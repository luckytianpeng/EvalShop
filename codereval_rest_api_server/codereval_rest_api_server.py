"""CodeEval REST API Server

Workflow:
    1. Start HTTPServer
    2. For every request:
        3. Only handle POST
            4. Check the Payload; do Authentication
            5. For every testing sample
                6. Set timeout
            7. Invoke the codereval_sandbox to run the testing samples
            8. Get the stderr info from the sandbox
            9. Return the response
"""
import sys
import getopt
import os
from pathlib import Path
import json
from json import JSONDecodeError
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import hashlib
import time
import traceback
import socket
import gc
import datetime
import logging

import docker


# For bash from another directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Logging
timestamp = f'{datetime.datetime.now()}'.replace(':', '-').replace('.', ' ')
dir_name, file_name = os.path.split(__file__)
file_handler = os.path.join('logging', f'{file_name} {timestamp}.log')
print(f'\n\nLogging file: "{file_handler}"\n\n')
logging.basicConfig(
        format='%(asctime)s [%(levelname)s] - [File "%(filename)s", ' \
                'line %(lineno)s, in %(funcName)s()] - %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(file_handler)
        ],
        level=logging.INFO
        )
log = logging.getLogger(__name__)


class CustomHandler(SimpleHTTPRequestHandler):
    """HTTP request handler.

    2. For every request:
    """

    def __send_delay(self, code, bytes_like_object, dealy_seconds):
        """Against malware scanning."""
        time.sleep(dealy_seconds)
        self.send_response(code)
        self.end_headers()
        self.wfile.write(bytes_like_object)

    def do_GET(self):
        config = json.load(open(
                'codereval_rest_api_server_config.json',
                'r',
                encoding='utf-8'))
        time.sleep(config['request_error_delay_time'])
        return

    # 3. Only handle POST
    def do_POST(self):
        config = json.load(open(
                'codereval_rest_api_server_config.json',
                'r',
                encoding='utf-8'))

        # 4. Check the Payload; do Authentication
        # Get Payload (json)
        if self.headers['Content-Type'] != 'application/json':
            self.__send_delay(
                    415,
                    'Unsupported Media Type'.encode(encoding='utf-8'),
                    config['request_error_delay_time'])
            return

        try:
            data = json.loads(
                    self.rfile.read(int(self.headers['content-length'])))
        except JSONDecodeError as e:
            self.__send_delay(
                    400,
                    'Bad Request'.encode(encoding='utf-8'),
                    config['request_error_delay_time'])
            return

        # Authentication:
        if 'api_key' not in data:
            self.__send_delay(
                    403,
                    'Forbidden'.encode(encoding='utf-8'),
                    config['request_error_delay_time'])
            return

        api_key_md5 = hashlib.md5(
                data['api_key'].encode('utf-8')).hexdigest()
        api_keys = json.load(open(
                'codereval_rest_api_server_api_keys.json',
                'r',
                encoding='utf-8'))
        '''Cancel Authentication:
        if api_key_md5 not in api_keys:
            self.__send_delay(
                    403,
                    'Forbidden'.encode(encoding='utf-8'),
                    config['request_error_delay_time'])
            return

        log.info(f'User: {api_keys[api_key_md5]}')
        '''

        # Check path
        if self.path != '/v2':
            self.__send_delay(
                    404,
                    'Not Found'.encode(encoding='utf-8'),
                    config['request_error_delay_time'])
            return

        # Check api_type
        if 'api_type' not in data \
                or data['api_type'] != 'CoderEval':
            self.__send_delay(
                    406,
                    'Not Acceptable'.encode(encoding='utf-8'),
                    config['request_error_delay_time'])
            return

        # Check api_version? Not yet.
        if not data['api_version'].startswith('1.'):
            self.__send_delay(
                    406,
                    'Not Acceptable'.encode(encoding='utf-8'),
                    config['request_error_delay_time'])
            return

        # Check samples
        if 'samples' not in data \
                or not data['samples']:
            self.__send_delay(
                    400,
                    'Bad Request'.encode(encoding='utf-8'),
                    config['request_error_delay_time'])
            return

        # 5. For every testing sample
        for sample in data['samples']:
            # Check:
            if 'ques_id' not in sample \
                    or not sample['ques_id'] \
                    or 'generate_results' not in sample \
                    or not sample['generate_results']:
                self.__send_delay(
                        400,
                        'Bad Request'.encode(encoding='utf-8'),
                        config['request_error_delay_time'])
                return
            
            generate_results = sample['generate_results']
            for g_r in generate_results:
                if 'generate_code' not in g_r \
                        or not g_r['generate_code']:
                    self.__send_delay(
                        400,
                        'Bad Request'.encode(encoding='utf-8'),
                        config['request_error_delay_time'])
                    return

            # 6. Set timeout
            if 'timeout'not in sample:
                sample['timeout'] = config['testing_timeout']

        # 7. Invoke the sandbox to run th the testing sample
        data['sandbox'] = {'name': config['sandbox_name']}
        
        st = time.time()
        # Ref:  
        # - https://docker-py.readthedocs.io/en/stable/api.html
        # - https://github.com/docker/compose/issues/6837

        docker_client = docker\
                .APIClient(timeout=config['sandbox_timeout'])
        docker_container = docker_client.create_container(
                image=config['sandbox_name'],
                stdin_open=True,
                runtime='runsc')
        docker_sock = docker_client\
                .attach_socket(
                        docker_container,
                        params={
                            "stdin": 1,
                            "stdout": 1,
                            "stderr": 1,
                            "stream": 1,
                        })
        try:
            docker_client.start(docker_container)
            docker_sock._sock.send(json.dumps(data['samples']).encode())
            docker_sock._sock.close()
            docker_sock.close()
            status = docker_client.wait(docker_container)

            # 8. Get the stderr info from the sandbox
            # Get result from sandbox
            docker_status_code = status["StatusCode"]
            docker_stdout = docker_client\
                    .logs(docker_container, stderr=False).decode()
            docker_stderr = docker_client\
                    .logs(docker_container,stdout=False).decode()

            docker_client.stop(docker_container)
            docker_client.wait(docker_container)

            # update data with result
            if docker_stderr:
                # Error on sandbox itself, not the test_code.
                data['sandbox']['stderr'] = docker_stderr
            else:
                docker_stdout_json = json.loads(docker_stdout)
                data['sandbox']['environment'] =\
                        docker_stdout_json['environment']
                data['sandbox']['analyse_stdin'] = \
                        docker_stdout_json['analyse_stdin']
                data['sandbox']['execute'] = docker_stdout_json['execute']
                data['samples'] =\
                        docker_stdout_json['samples']

            et = time.time()
            elapsed_time = et - st
            data['sandbox']['elapsed_time'] = elapsed_time
        except:
            # Timeout exception of Docker will be capture here.
            # print(traceback.format_exc())
            data['sandbox']['stderr'] = traceback.format_exc()
        finally:
            docker_client.remove_container(docker_container)
            docker_client.close()
            docker_sock.close()

        # 9. Return the response
        data['status_code'] = 200
        data['status_message'] = 'OK'
        # Remove api_key for safety.
        del data['api_key']

        try:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode(encoding='utf-8'))
        except:
            pass

        gc.collect()
        return


def get_local_IP_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_addr = s.getsockname()[0]
    s.close()
    return ip_addr


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error as msg:
            raise Usage(msg)
        # more code, unchanged
    except Usage as err:
        log.exception(err.msg)
        print("for help use --help", file=sys.stderr)
        return 2

    config = json.load(open(
            'codereval_rest_api_server_config.json',
            'r',
            encoding='utf-8'))

    # 1. Start HTTPServer
    server = ThreadingHTTPServer(tuple(config['server_address']), CustomHandler)
    log.info(f'CoderEval REST API Server is running at ' \
            f'http://{get_local_IP_address()}:' \
            f'{config["server_address"][1]}')
    print('\nQuit the server with CTRL-C\n')
    try:
        server.serve_forever()
    except KeyboardInterrupt:  # Ctrl-C
        pass
    
    server.server_close()
    print()
    log.info('CoderEval REST API Server has stopped.')

    return 0


if __name__ == "__main__":
    sys.exit(main())
