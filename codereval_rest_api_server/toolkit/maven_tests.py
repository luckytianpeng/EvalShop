"""
E.g.:
hasor-master/hasor-commons/src/main/java/net/hasor/utils/ResourcesUtils.java
hasor-master/hasor-commons/src/test/java/net/hasor/utils/ResourcesUtilsTest.java


1. CoderEval4Java.json
    file_name: xxx.java
    package: net.hasor.utils
    
2. path
        src/
            main/
                xxx.java
            test/
                xxxTest.java
"""
import os
import json
import glob


CODER_EVAL_JAVA_FILE = \
      '../codereval_sandbox/github/CoderEval/CoderEval4Java.json'

output = {}
file_count = 0
test_count = 0

codereval_java = json.load(open(CODER_EVAL_JAVA_FILE, 'r', encoding='utf-8'))
for record in codereval_java['RECORDS']:
    _id = record['_id']
    project = record['project']
    file_name = record['file_name']
    package = record['package'].replace('.', '/')

    if project not in output:
        output[project] = {
                'project_local_dir': '',
                'records': []}

    project_local_dir = os.path.join(
            '../codereval_sandbox/github/', project)

    if os.path.exists(project_local_dir):
        output[project]['project_local_dir'] = project_local_dir

        pathname_pattern = f'{project_local_dir}/**/{package}/{file_name}'
        found_files = glob.glob(pathname_pattern, recursive=True)
        assert len(found_files) <= 1
        for ff in found_files:
            file_count = file_count + 1

            if '/src/main/' in ff:
                head, tail = os.path.split(ff)
                fn, fe = os.path.splitext(tail)

                # hasor-master/hasor-commons/src/test/java/net/hasor/utils/ResourcesUtilsTest.java
                # hasor-master/hasor-commons/src/main/java/net/hasor/utils/ResourcesUtils.java
                test_pattern = f'{head.replace("/src/main/", "/src/test/")}/{package}/*{fn}*{fe}'

                found_tests = glob.glob(test_pattern, recursive=True)
                if len(found_tests) == 0:
                    output[project]['records'].append(
                        {'_id': _id, 'file': ff, 'test': ''})

                for t in found_tests:
                    test_count = test_count + 1
                    output[project]['records'].append(
                            {'_id': _id, 'file': ff, 'test': t})
            else:
                output[project]['records'].append(
                      {'_id': _id, 'file': ff, 'test': ''})
    else:
        pass

print(json.dumps(output, indent=4, sort_keys=False))
