import os
import sys
import json
import time
import shutil
import traceback

from virtualenvironmentapi import VirtualEnvironment
from utility import execute

import git


TIMEOUT = 60 * 3


# For bash from another directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

all_projects = json.load(open(
      './projects.json',
      'r',
      encoding='utf-8'))

project_total = len(all_projects)
project_count = 0
test_count = 0
passed_test_count = 0
exit_code = 0

st = time.time()
for project in all_projects:
    if project['language'] != 'python':
        continue

    project_count = project_count + 1

    project_local_dir = os.path.join(
            './codereval_sandbox/github/', project['project'])
    assert os.path.exists(project_local_dir)

    try:
        local_repo = git.Repo(project_local_dir)
        # checks out the current index for the current directory, 
        # throwing away all changes in files from the current 
        # directory downwards
        local_repo.git.checkout('.')
    except:
        print(traceback.format_exc(), file=sys.stderr)
        continue

    print(f'{"-" * 80}')
    print(f'{project_count}/{project_total}\t{project["project"]}')

    for id in project['_ids']:
        test_count = test_count + 1
        print(f'\t{"-" * 40}')
        print(f'\t{test_count}\t{id}')

        test_file = os.path.join(
                './codereval_sandbox/test_entry_points', f'{id}.py')
        if os.path.isfile(test_file):
            # passed_test_count = passed_test_count + 1

            shutil.copyfile(
                test_file,
                os.path.join(project_local_dir, f'{id}.py'))
            
            # Activate the virutal environment and run test with original code:
            venv_name = 'env-auto'
            venv_path = os.path.join(project_local_dir, venv_name)

            # Create the virtual environment if it does not exist:
            env = VirtualEnvironment(
                    working_directory=project_local_dir,
                    venv_name=venv_name)
            assert env.is_available

            result = env.system(f'python {id}.py')
            if not result['stderr']:
                passed_test_count = passed_test_count + 1
            else:
                print(f'{result["stderr"]}')

et = time.time()
print(f'elapsed_time: {et - st} S; ' \
        f'{passed_test_count}/{test_count}={passed_test_count/test_count}')

exit_code = 0
exit(exit_code)
