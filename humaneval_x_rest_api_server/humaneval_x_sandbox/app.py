"""Application inside docker

Functions:
- Check the environment
- Read samples (generated_codes) from stdin
- Compile and execute
- Write the results to stderr
"""

import sys
import getopt
import os
import traceback
import json
from datetime import datetime
import time
from subprocess import Popen, PIPE, TimeoutExpired
from threading import Timer
import signal


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
        print(err.msg, file=sys.stderr)
        print("for help use --help", file=sys.stderr)
        return 2

    # Do ...
    result = {}

    environment = {
        'Hardware Model': {
            'value': '',
            'command': 'cat /sys/devices/virtual/dmi/id/product_name'
        },
        'Architecture': {
            'value': '',
            'command': 'uname -m'
        },
        'Operating System': {
            'value': '',
            'command': 'grep -ioP \'^PRETTY_NAME=\\K.+\' /etc/os-release'
        },
        'Kernel': {
            'value': '',
            'command': 'uname -sr'
        },
        'cpuinfo': {
            'value': '',
            'command': 'cat /proc/cpuinfo'
        },
        'meminfo': {
            'value': '',
            'command': 'cat /proc/meminfo'
        }
    }

    # environment
    environment['Hardware Model']['value'] =\
            os.popen(environment['Hardware Model']['command']).read()\
                .rstrip()
    environment['Architecture']['value'] =\
            os.popen(environment['Architecture']['command']).read()\
                .rstrip()
    environment['Operating System']['value'] =\
            os.popen(environment['Operating System']['command'])\
                .read().rstrip().replace('\"', '')
    environment['Kernel']['value'] =\
            os.popen(environment['Kernel']['command']).read()\
                .rstrip()
    environment['cpuinfo']['value'] =\
            os.popen(environment['cpuinfo']['command']).read()
    environment['meminfo']['value'] =\
            os.popen(environment['meminfo']['command']).read()
    environment['python'] =\
            os.popen('python3 --version').read().rstrip()
    environment['jdk'] =\
            os.popen('java --version').read().rstrip()
    environment['c++'] =\
            os.popen('c++ --version').read().rstrip()
    environment['g++'] =\
            os.popen('g++ --version').read().rstrip()
    environment['boost'] =\
            os.popen('cat /usr/include/boost/version.hpp | grep \'#define BOOST_LIB_VERSION\'').read().rstrip()
            # os.popen('dpkg -s libboost-dev | grep "Version"').read().rstrip()
    environment['openssl'] =\
            os.popen('openssl version').read().rstrip()

    result['environment'] = environment

    # read_stdin
    stdin_lines = ''.join([line for line in sys.stdin])
    result['read_stdin'] = {
        "exit_code": 0,
        # "stdin": stdin_lines,  # If stdin is bytes, there will be trouble
        "stdout": "",
        "stderr": ""
    }

    # analyse_stdin
    result['analyse_stdin'] = {
        "exit_code": 0,
        "stdin_json": None,
        "stdout": "",
        "stderr": ""
    }

    generated_codes = {}

    try:
        generated_codes = json.loads(stdin_lines, strict=False)
        # Check every sample
        for generated_code in generated_codes:
            task_id = generated_code['task_id']
            testing_code = generated_code['testing_code']
            timeout = generated_code['timeout']
    except:
        result['analyse_stdin']['exit_code'] = 1
        result['analyse_stdin']['stderr'] = traceback.format_exc()
        print(json.dumps(result))
        return 1

    for generated_code in generated_codes:
        task_id = generated_code['task_id']
        testing_code = generated_code['testing_code']
        timeout = generated_code['timeout']

        language, _ = task_id.lower().split('/')

        language_filename_map = {
            'python': 'test.py',
            'java': 'Main.java',
            'cpp': 'test.cpp'
        }

        # save_file
        with open(language_filename_map[language], 'w') as file:
            file.write(testing_code)
        generated_code["save_file"] = {
            "file_path": language_filename_map[language],
            "exit_code": 0,
            "stdout": "",
            "stderr": ""
        }

        # compile
        generated_code["compile"] = {
            "command": "",
            "exit_code": 0,
            "stdout": "",
            "stderr": "",
            "elapsed_time": 0
        }

        compile_command = []
        if language == 'python':
            pass
        elif language == 'java':
            compile_command = ['javac', language_filename_map[language]]
        elif language == 'cpp':
            compile_command = [
                    'g++', '-std=c++11', '-o', 'test',
                    language_filename_map[language], '-lcrypto', '-lssl']
        else:
            pass

        if language in ['java', 'cpp']:
            st = time.time()
            process = Popen(compile_command, stdout=PIPE, stderr=PIPE)
            try:
                return_code = process.wait(timeout=timeout)
                stdout, stderr = process.communicate()
                et = time.time()
                generated_code["compile"] = {
                    "command": ' '.join(compile_command),
                    "exit_code": process.returncode,
                    "stdout": stdout.decode(),
                    "stderr": stderr.decode(),
                    "elapsed_time": et - st
                }
            except TimeoutExpired:
                generated_code["compile"] = {"timeout": timeout}
                generated_code["compile"]['stderr'] = traceback.format_exc()
                os.kill(process.pid, signal.SIGTERM)
            except:
                generated_code["compile"]['stderr'] = traceback.format_exc()
            finally:
                process.kill()

        # execute
        if not generated_code["compile"]['stderr']:
            generated_code["execute"] = {
                "command": "",
                "exit_code": 0,
                "stdout": "",
                "stderr": "",
                "elapsed_time": 0
            }
            execute_command = []
            if language == 'python':
                execute_command = ['python3', language_filename_map[language]]
            elif language == 'java':
                execute_command = ['java', 'Main']
            elif language == 'cpp':
                execute_command = ['./test']
            else:
                pass

            st = time.time()
            process = Popen(execute_command, stdout=PIPE, stderr=PIPE)
            try:
                return_code = process.wait(timeout=timeout)
                stdout, stderr = process.communicate()
                et = time.time()
                generated_code["execute"] = {
                    "command": ' '.join(execute_command),
                    "exit_code": process.returncode,
                    "stdout": stdout.decode(),
                    "stderr": stderr.decode(),
                    "elapsed_time": et - st
                }
            except TimeoutExpired:
                generated_code["execute"] = {"timeout": timeout}
                generated_code["execute"]['stderr'] = traceback.format_exc()
                os.kill(process.pid, signal.SIGTERM)
            except:
                generated_code["execute"]['stderr'] = traceback.format_exc()
            finally:
                process.kill()

    result['generated_codes'] = generated_codes
    print(json.dumps(result))

    return 0


if __name__ == "__main__":
    sys.exit(main())
