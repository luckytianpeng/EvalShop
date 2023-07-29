"""
62ece4982e6aefcf4aabbd70
cloudmesh/cloudmesh-common
cloudmesh/common/systeminfo.py
os_is_mac
45
52


Checks if the os is macOS

    :return: bool, True is macOS, otherwise False.

"""
import sys
import traceback
import pickle

# import ...
from cloudmesh.common.systeminfo import os_is_mac

# Test Data
# test_data = 

#
exit_code = 0

try:
    result = os_is_mac()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
