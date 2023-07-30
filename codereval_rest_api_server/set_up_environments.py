import sys
import os
import json
import time
import shutil
import traceback
from subprocess import Popen, PIPE, TimeoutExpired
import glob

from virtualenvironmentapi import VirtualEnvironment


TIMEOUT = 60 * 3


# For bash from another directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

all_projects = json.load(open(
      './projects.json',
      'r',
      encoding='utf-8'))

total = len(all_projects)
count = 0
exit_code = 0

st = time.time()
for project in all_projects:
    count = count + 1
    
    print(f'{"-" * 80}')
    print(f'{count}/{total}\t{project["project"]}')

    project_local_dir = os.path.join(
          './codereval_sandbox/github/', project['project'])
    assert os.path.exists(project_local_dir)

    requirements_files = glob.glob(
          os.path.join(project_local_dir, '*requirements*.txt'))
    tox_ini_file = os.path.join(project_local_dir, 'tox.ini')

    packages = []
    try:
        for test in project['tests']:
            packages += test['install']
        packages = list(set(packages))
    except:
        pass

    if len(requirements_files) == 0 \
            and not os.path.isfile(tox_ini_file) \
            and not packages:
        continue
    
    venv_name = 'env-auto'
    venv_path = os.path.join(project_local_dir, venv_name)
    # Clean
    shutil.rmtree(venv_path, ignore_errors=True)

    # Create the virtual environment if it does not exist:
    env = VirtualEnvironment(project_local_dir, 'python3', venv_name)
    assert env.is_available
    assert os.path.isfile(os.path.join(venv_path, 'bin/activate'))
    
    print(f'requirements_files:\n\t{requirements_files}')
    for r_f in requirements_files:        
        print(f'\t\tinstall -r {r_f}')
        try:
            env.install(f'-r {r_f}', timeout=TIMEOUT)
        except:
            exit_code = 1
            print(f'\t\t{traceback.format_exc()}')
            break

    print(f'tox_ini_file:\n\t{tox_ini_file}')
    if os.path.isfile(tox_ini_file):
        print(f'\t\tinstall tox')
        try:
            env.install('tox', timeout=TIMEOUT)
        except:
            exit_code = 1
            print(f'\t\t{traceback.format_exc()}')
            break

    print(f'packages:\n\t{packages}')
    for package in packages:
        print(f'\t\tinstall {package}')
        try:
            env.install(package, timeout=TIMEOUT)
        except:
            exit_code = 1
            print(f'\t\t{traceback.format_exc()}')
            break

et = time.time()
print(f'elapsed_time: {et - st} S')

exit(exit_code)
