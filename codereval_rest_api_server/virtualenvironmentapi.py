"""Virtual Environment API

Ref:  
- https://pypi.org/project/virtualenv-api/

However, there is a bug in "virtualenv-api":
    subprocess.CalledProcessError: Command '<Popen: returncode: -11 args: ['bin/python', '-m', 'pip', '-V']>' died with <Signals.SIGSEGV: 11>.

Ref:
- https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

    python3 -m pip install --user virtualenv

    python3 -m venv env-manual
"""
from typing import List
from typing import Tuple

import sys
import os
import shlex
import traceback
from subprocess import Popen, PIPE, TimeoutExpired
# import signal


TIMEOUT = 60 * 1

class VirtualEnvironment:
    __license__ = 'GNU GENERAL PUBLIC LICENSE Version 3 - ' \
            'https://www.gnu.org/licenses/gpl-3.0.en.html'
    __author__ = 'Peng Tian'
    __email__ = 'luckytianpeng@hotmail.com'

    def __exec(command='', timeout=TIMEOUT) -> dict:
        result = {
            'exit_code': 1,
            'stdout': '',
            'stderr': '',
            'timeout': '',
            'except': ''
        }

        process = Popen(
              shlex.split(command), 
              shell=False,
              stdout=PIPE,
              stderr=PIPE)
        try:
            result['exit_code'] = process.wait(timeout=timeout)
            stdout, stderr = process.communicate()
            result['stdout'] = stdout.decode()
            result['stderr'] = stderr.decode()
        except TimeoutExpired:
            result['timeout'] = traceback.format_exc()
            result['exit_code'] = 1
        except:
            result['except'] = traceback.format_exc()
            result['exit_code'] = 1
        finally:
            process.kill()

        return result

    def __init__(
            self,
            working_directory='./',
            python='python3',
            venv_name='./',
            timeout=TIMEOUT) -> None:
        self.working_directory = working_directory
        self.venv_name = venv_name
        self.timeout = timeout
        self.is_available = True

        venv_path = os.path.join(self.working_directory, self.venv_name)

        if os.path.exists(venv_path):
            pass
        else:
            command = f'{python} -m venv {venv_path}'
            result = VirtualEnvironment.__exec(command)
            if result['exit_code'] != 0:
                self.is_available = False
            

    def system(self, command='', timeout=None) -> dict:
        if not timeout:
            timeout = self.timeout

        cmd = f'''\
/bin/bash -c \
"cd {self.working_directory} \
&& source ./{self.venv_name}/bin/activate \
&& {command} \
&& deactivate"'''
        return VirtualEnvironment.__exec(cmd, timeout)

    @property
    def python_version(self) -> str:
        result = self.system('python --version')
        return result['stdout'].strip()
    
    @property
    def pip_version(self) -> str:
        result = self.system('pip --version')
        return result['stdout'].strip()

    @property
    def installed_packages(self) -> List[Tuple[str, str]]:
        result = self.system('pip list --format=columns')
        return [tuple(line.split())
                for line in result['stdout'].strip().split('\n')[2:]]
    
    @property
    def installed_package_names(self) -> List[str]:
        return [i[0] for i in self.installed_packages]

    def is_installed(self, package) -> bool:
        return package in self.installed_package_names

    def install(self, package_or_file, timeout=None) -> dict:
        return self.system(f'pip install {package_or_file}', timeout)
