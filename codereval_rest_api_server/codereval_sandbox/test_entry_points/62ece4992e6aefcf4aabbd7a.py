"""
62ece4992e6aefcf4aabbd7a
cloudmesh/cloudmesh-common
cloudmesh/common/util.py
is_gitbash
177
187


Check whether the current program is run in a Windows gitbash terminal

    Returns:
            boolean, True if gitbash else False

"""
import sys
import traceback
import pickle

# import ...
from cloudmesh.common.util import is_gitbash

# Test Data
# test_data = 

#
exit_code = 0

try:
    result = is_gitbash()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
