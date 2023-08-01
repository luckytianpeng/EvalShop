"""
"""
import os
import traceback
from subprocess import Popen, PIPE, TimeoutExpired
import signal
import shlex


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
