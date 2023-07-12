"""CodeGeeX REST API Server

Workflow:
    1. Start CodeGeeX
    2. Start HTTPServer
    3. For every request:
        4. Only handle POST
            5. Check the Payload; do Authentication
            6. Generate codes
            7. Return the response
"""
import time
import argparse
import traceback
import json
from json import JSONDecodeError
import os
import gc
import hashlib
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import datetime
import logging

import torch
# import numpy as np

import codegeex
from codegeex.torch import CodeGeeXModel
from codegeex.tokenizer import CodeGeeXTokenizer
from codegeex.quantization import quantize


timestamp = f'{datetime.datetime.now()}'.replace(':', '-').replace('.', ' ')
dir_name, file_name = os.path.split(__file__)
file_handler = os.path.join(dir_name, 'logging', f'{file_name} {timestamp}.log')
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


def model_provider(args):
    """Build the model."""

    model = CodeGeeXModel(
        args.hidden_size,
        args.num_layers,
        args.num_attention_heads,
        args.padded_vocab_size,
        args.max_position_embeddings
    )
    
    return model


def add_code_generation_args(parser):
    group = parser.add_argument_group(title="code generation")
    group.add_argument(
        "--num-layers",
        type=int,
        default=39,
    )
    group.add_argument(
        "--hidden-size",
        type=int,
        default=5120,
    )
    group.add_argument(
        "--num-attention-heads",
        type=int,
        default=40,
    )
    group.add_argument(
        "--padded-vocab-size",
        type=int,
        default=52224,
    )
    group.add_argument(
        "--max-position-embeddings",
        type=int,
        default=2048,
    )
    group.add_argument(
        "--temperature",
        type=float,
        default=1.0,
        help="Sampling temperature.",
    )
    group.add_argument(
        "--greedy",
        action="store_true",
        default=False,
        help="Use greedy sampling.",
    )
    group.add_argument(
        "--top-p",
        type=float,
        default=0.0,
        help="Top p sampling.",
    )
    group.add_argument(
        "--top-k",
        type=int,
        default=0,
        help="Top k sampling.",
    )
    group.add_argument(
        "--out-seq-length",
        type=int,
        default=2048,
        help="Size of the output generated text.",
    )
    group.add_argument(
        "--prompt-file",
        type=str,
        default="./test_prompt.txt",
    )
    group.add_argument(
        "--tokenizer-path",
        type=str,
        default="./tokenizer",
    )
    group.add_argument(
        "--load",
        type=str,
    )
    group.add_argument(
        "--state-dict-path",
        type=str,
    )
    group.add_argument(
        "--micro-batch-size",
        type=int,
        default=1,
    )
    group.add_argument(
        "--quantize",
        action="store_true",
    )
    group.add_argument(
        "--interative",
        action="store_true",
    )
    
    return parser


def MakeHandlerClassFromArgv(codegeex_args, model, tokenizer):
    class CustomHandler(BaseHTTPRequestHandler):
        """HTTP request handler.

        3. For every request:
        """

        def __init__(self, *args, **kwargs):
            super(CustomHandler, self).__init__(*args, **kwargs)
            self.codegeex_args = codegeex_args.copy()
            self.model = model
            self.tokenizer = tokenizer

        def __send_delay(self, code, bytes_like_object, dealy_seconds):
            """Against malware scanning."""
            time.sleep(dealy_seconds)
            self.send_response(code)
            self.end_headers()
            self.wfile.write(bytes_like_object)

        def do_GET(self):
            config = json.load(open(
                    f'{os.path.dirname(__file__)}' \
                            '/codegeex_rest_api_server_config.json',
                    'r',
                    encoding='utf-8'))
            time.sleep(config['request_error_delay_time'])
            return

        # 4. Only handle POST
        def do_POST(self):
            config = json.load(open(
                    f'{os.path.dirname(__file__)}' \
                            '/codegeex_rest_api_server_config.json',
                    'r',
                    encoding='utf-8'))

            # 5. Check the Payload; do Authentication
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
                    f'{os.path.dirname(__file__)}' \
                            '/codegeex_rest_api_server_api_keys.json',
                    'r',
                    encoding='utf-8'))
            if api_key_md5 not in api_keys:
                self.__send_delay(
                        403,
                        'Forbidden'.encode(encoding='utf-8'),
                        config['request_error_delay_time'])
                return

            # Check api_type
            if 'api_type' not in data \
                    or data['api_type'] != 'codegeex':
                self.__send_delay(
                        406,
                        'Not Acceptable'.encode(encoding='utf-8'),
                        config['request_error_delay_time'])
                return

            # Check api_version.
            # For "1.x.x.x", return string; for "2.x.x.x", return json.
            if not data['api_version'].startswith('2.'):
                self.__send_delay(
                        406,
                        'Not Acceptable'.encode(encoding='utf-8'),
                        config['request_error_delay_time'])
                return

            # Check prompt
            if 'prompt' not in data \
                    or not data['prompt']:
                self.__send_delay(
                        400,
                        'Bad Request'.encode(encoding='utf-8'),
                        config['request_error_delay_time'])
                return

            new_codegeex_args = codegeex_args.copy()
            if 'args' in data:
                new_codegeex_args.update(data['args'])

            log.info(f'User: {api_keys[api_key_md5]}')
            log.info(json.dumps(new_codegeex_args, indent=4, sort_keys=True))

            result = {
                'stdout': '',
                'stderr': '',
                'elapsed_time': 0
            }

            content = {
                "api_version": "2.1.0.0",
                "api_type": "codegeex",
                "id": data['id'],
                "status_code": 200,
                "status_message": "OK",
                "response": result
            }

            # 6. Generate codes
            try:
                t0 = time.perf_counter()
                generated_code = codegeex.generate(
                    model,
                    tokenizer,
                    data['prompt'],
                    out_seq_length=new_codegeex_args['out_seq_length'],
                    seq_length=new_codegeex_args['max_position_embeddings'],
                    top_k=new_codegeex_args['top_k'],
                    top_p=new_codegeex_args['top_p'],
                    temperature=new_codegeex_args['temperature'],
                    micro_batch_size=new_codegeex_args['micro_batch_size'],
                    backend=new_codegeex_args['backend'],
                    verbose=new_codegeex_args['verbose'],
                )
                t1 = time.perf_counter()
                result['stdout'] = generated_code
                result['elapsed_time'] = t1 - t0
                log.info(f'Total generation time: {result["elapsed_time"]}')
            except (ValueError, FileNotFoundError) as e:
                result['stderr'] = e

            # 7. Return the response
            try:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(content).encode(encoding='utf-8'))
            except:
                log.exception(traceback.format_exc())

            gc.collect()
            return

    return CustomHandler


def main():
    # Read server-config
    parser = argparse.ArgumentParser()
    parser = add_code_generation_args(parser)
    args, _ = parser.parse_known_args()
    
    codegeex_args = vars(args)
    log.info('CodeGeeX starts with:\n{}' \
            .format(json.dumps(codegeex_args, indent=4, sort_keys=True)))

    # 1. Start CodeGeeX
    log.info("Loading tokenizer ...")
    tokenizer = CodeGeeXTokenizer(
        tokenizer_path=args.tokenizer_path, 
        mode="codegeex-13b")

    log.info("Loading state dict ...")
    state_dict = torch.load(args.load, map_location="cpu")
    state_dict = state_dict["module"]

    log.info("Building CodeGeeX model ...")
    model = model_provider(args)
    model.load_state_dict(state_dict)
    model.eval()
    model.half()
    if args.quantize:
        model = quantize(model, weight_bit_width=8, backend="torch")
    model.cuda()
    torch.cuda.synchronize()
    
    with open(args.prompt_file, "r") as f:
        prompt = f.readlines()
        prompt = "".join(prompt)
    
    out_seq_lengths = [args.out_seq_length]
    # for out_seq_length in out_seq_lengths:
    log.info(f"Generating with out_seq_len {out_seq_lengths}... No, infinite!")

    # 2. Start HTTPServer
    config = json.load(
            open(f'{os.path.dirname(__file__)}' \
                '/codegeex_rest_api_server_config.json', 'r', encoding='utf-8'))
    log.info(f'CodeGeeX REST API Server is running at ' \
            f'http://{socket.gethostbyname(socket.gethostname())}:' \
            f'{config["server_address"][1]}')
    print('\nQuit the server with CTRL-C\n')
    request_handler = MakeHandlerClassFromArgv(codegeex_args, model, tokenizer)
    server = HTTPServer(tuple(config['server_address']), request_handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:  # Ctrl-C
        pass

    server.server_close()
    print()
    log.info('CodeGeeX REST API Server has stopped.')


if __name__ == "__main__":
    main()
