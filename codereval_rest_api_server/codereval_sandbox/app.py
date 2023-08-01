"""Application inside docker

Functions:
- Check the environment
- Read samples (generated_codes) from stdin
- Compile and execute
- Write the results to stderr
"""

"""Run in docker

apt -y install git
pip install GitPython

# Ref:  https://pypi.org/project/virtualenv-api/
apt -y install python3-virtualenv
pip install virtualenv-api
"""
import sys
import getopt
import os
import json
import traceback
from subprocess import Popen, PIPE, TimeoutExpired
import signal
import shlex
import re
import time
import shutil

import git
# from virtualenvapi.manage import VirtualEnvironment


TEST_ENTRY_POINTS_DIR = './test_entry_points/'
GITHUB_LOCAL_DIR = './github'


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def execute(command, timeout):
    result = {
        'exit_code': 0,
        'stdout': '',
        'sterr': ''
    }

    process = Popen(
            shlex.split(command), shell=False, stdout=PIPE, stderr=PIPE)
    try:
        result['exit_code'] = process.wait(timeout=timeout)
        stdout, stderr = process.communicate()
        result['stdout'] = stdout.decode()
        result['stderr'] = stderr.decode()
    except TimeoutExpired:
        # print(traceback.format_exc(), file=sys.stderr)
        os.kill(process.pid, signal.SIGTERM)
        result['exit_code'] = 1
        result['stderr'] = traceback.format_exc()
    except:
        # print(traceback.format_exc(), file=sys.stderr)
        result['exit_code'] = 1
        result['stderr'] = traceback.format_exc()
    finally:
        process.kill()

    return result

def exectue_test_entry_point(
        generate_code,
        test_entry_point_file_name,
        test_entry_point_file_full_path,
        timeout):
    with open(test_entry_point_file_full_path, 'r') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    # print(lines)

    ques_id = lines[1]
    project = lines[2]
    file_path = lines[3]
    name = lines[4]
    lineno = lines[5]
    end_lineno = lines[6]
    
    result = {
        'exit_code': 1,
        'stdout': '',
        'stderr': '',
        'elapsed_time': 0,
        'return_code': 1,
        'is_pass': False
    }

    try:
        lineno = int(lineno)
    except ValueError:
        result['stderr'] = f'lineno = {lineno} is not int'
        return result

    try:
        end_lineno = int(end_lineno)
    except ValueError:
        result['stderr'] = f'end_lineno = {end_lineno} is not int'
        return result

    if lineno >= end_lineno:
        result['sterr'] = f'lineno:{lineno}, end_lineno:{end_lineno}'
        return result

    project_local_dir = os.path.join(GITHUB_LOCAL_DIR, project)
    
    try:
        local_repo = git.Repo(project_local_dir)
        # checks out the current index for the current directory, 
        # throwing away all changes in files from the current 
        # directory downwards
        local_repo.git.checkout('.')
    except:
        result['stderr'] = traceback.format_exc()
        return result

    file_full_path = os.path.join(project_local_dir, file_path)
    if not os.path.exists(file_full_path):
        result['stderr'] = f'{file_full_path} doese not exit'
        return result
    
    with open(file_full_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    original_code = ''.join(lines[lineno - 1 : end_lineno])

    if end_lineno > len(lines):
        result['stderr'] = f'{end_lineno} > {len(lines)}'
        return result

    shutil.copyfile(
        test_entry_point_file_full_path,
        os.path.join(project_local_dir, test_entry_point_file_name))
    
    # Activate the virutal environment and run test with original code:
    venv_path = f'{project_local_dir}/env-auto'
    test_cmd = f'python {project_local_dir}/{test_entry_point_file_name}'
    cmd = f'/bin/bash -c "source {venv_path}/bin/activate && {test_cmd}"'

    original_result = execute(cmd, timeout)

    # Activate the virutal environment and run test with generated code:
    # Inject the generated code:

    indentation = original_code \
            [:len(original_code) - len(original_code.lstrip())]

    processed_code = [
            indentation + line  + '\n'
            for line in generate_code.split('\n')]
    # print(''.join(processed_code))

    # Inject:
    lines[lineno - 1: end_lineno] = processed_code
    with open(file_full_path, 'w') as f:
        f.write(''.join(lines))
    
    generated_result = execute(cmd, timeout)
    result['exit_code'] = generated_result['exit_code']
    result['stdout'] = generated_result['stdout']
    result['stderr'] = generated_result['stderr']

    result['is_pass'] = True
    result['return_code'] = generated_result['exit_code']
    if generated_result['stderr'] != '' \
            or original_result['stdout'] != generated_result['stdout']:
        result['is_pass'] = False

    try:
        local_repo = git.Repo(project_local_dir)
        # checks out the current index for the current directory, 
        # throwing away all changes in files from the current 
        # directory downwards
        local_repo.git.checkout('.')
    except:
        pass

    return result


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
    #environment['jdk'] =\
    #        os.popen('java --version').read().rstrip()
    #environment['c++'] =\
    #        os.popen('c++ --version').read().rstrip()
    #environment['g++'] =\
    #        os.popen('g++ --version').read().rstrip()
    #environment['boost'] =\
    #        os.popen('cat /usr/include/boost/version.hpp | grep \'#define BOOST_LIB_VERSION\'').read().rstrip()
    #        # os.popen('dpkg -s libboost-dev | grep "Version"').read().rstrip()
    #environment['openssl'] =\
    #        os.popen('openssl version').read().rstrip()

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

    samples = {}
    # Check every sample
    try:
        samples = json.loads(stdin_lines, strict=False)
        for sample in samples:
            ques_id = sample['ques_id']
            generate_results = sample['generate_results']
            for g_r in generate_results:
                generate_code = g_r['generate_code']
                is_pass = g_r['is_pass']
                return_code = g_r['return_code']
    except:
        result['analyse_stdin']['exit_code'] = 1
        result['analyse_stdin']['stderr'] = traceback.format_exc()
        result['samples'] = []
        print(json.dumps(result))
        return 1

    #
    result['execute'] = {
        "exit_code": 0,
        "stdout": "",
        "stderr": ""
    }

    try:
        # Execute
        for sample in samples:
            generate_results = sample['generate_results']
            for g_r in generate_results:
                g_r['exit_code'] = 1
                g_r['return_code'] = 1
                g_r['stdout'] = ''
                g_r['stderr'] = ''
                g_r['is_pass'] = False

            ques_id = sample['ques_id']

            test_entry_point_file_name = f'{sample["ques_id"]}.py'
            test_entry_point_file_full_path = os.path.join(
                    TEST_ENTRY_POINTS_DIR,
                    test_entry_point_file_name
                    )

            sample['exit_code'] = 0
            sample['stdout'] = ''
            sample['stderr'] = ''
            if os.path.exists(test_entry_point_file_full_path):
                generate_results = sample['generate_results']
                for g_r in generate_results:
                    generate_code = g_r['generate_code']

                    st = time.perf_counter()
                    exe_result = exectue_test_entry_point(
                            generate_code,
                            test_entry_point_file_name,
                            test_entry_point_file_full_path,
                            sample['timeout'])
                    et = time.perf_counter()
                    g_r['elapsed_time'] = et - st

                    g_r['exit_code'] = exe_result['exit_code']
                    g_r['return_code'] = exe_result['exit_code']
                    g_r['stdout'] = exe_result['stdout']
                    g_r['stderr'] = exe_result['stderr']
                    g_r['is_pass'] = exe_result['is_pass']
            else:
                sample['exit_code'] = 1
                sample['stderr'] = 'No test entry point'
    except:
        result['execute']['exit_code'] = 1
        result['execute']['stderr'] = traceback.format_exc()

    result['samples'] = samples
    print(json.dumps(result))

    return 0


if __name__ == "__main__":
    sys.exit(main())
