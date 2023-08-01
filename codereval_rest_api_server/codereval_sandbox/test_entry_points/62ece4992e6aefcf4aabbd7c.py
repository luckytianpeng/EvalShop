"""
62ece4992e6aefcf4aabbd7c
cloudmesh/cloudmesh-common
cloudmesh/common/Shell.py
oneline
449
458


Convert a script to one line command with the given seperator.

        Args:
                script: str
                separator: str
        Returns:
                str, the one-line command.

"""
import sys
import traceback
import pickle

# import ...
from cloudmesh.common.Shell import Shell


# Test Data
test_data = '''\
cd ~/project \n\
source ./env/bin/activate \n\
python test.py \n\
deactivate'''

#
exit_code = 0

try:
    result = Shell.oneline(test_data)
    # print(test_data)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
