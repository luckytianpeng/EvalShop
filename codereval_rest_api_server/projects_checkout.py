import sys
import os
import json
import time
import shutil
import traceback

import git


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
    print(f'{count}/{total}, {project["project"]} ({project["language"]})')

    project_local_dir = os.path.join(
          './codereval_sandbox/github/', project['project'])

    # Clean the local dir of project
    shutil.rmtree(project_local_dir, ignore_errors=True)

    if not os.path.exists(project_local_dir):
        os.makedirs(project_local_dir)
        # Ensure that the local dir is ready:
        assert os.path.exists(project_local_dir)

        try:
            t0 = time.time()

            repo = git.Repo.clone_from(
                  project['github_ssh'],
                  project_local_dir,
                  branch=project['branch']
                  )

            t1 = time.time()
            print(f'\tgit clone: {t1 - t0} S')
        except:
            exit_code = 1
            print(f'{project["project"]}, failed.', file=sys.stderr)
            print(traceback.format_exc(), file=sys.stderr)
            # Clean the local dir of project
            shutil.rmtree(project_local_dir, ignore_errors=True)
            break
    
    # git reset <commit_id>
    try:
        local_repo = git.Repo(project_local_dir)
        if str(local_repo.heads[project["branch"]].commit)\
                != project['commit_id']:
            t0 = time.time()

            # local_repo.git.reset(project['commit_id'])
            local_repo.git.checkout(project['commit_id'])

            t1 = time.time()
            print(f'\tgit checkout: {t1 - t0} S')
    except:
        exit_code = 1
        print(f'{project["project"]}, failed.', file=sys.stderr)
        print(traceback.format_exc(), file=sys.stderr)
        break

et = time.time()
print(f'elapsed_time: {et - st} S')

exit(exit_code)
