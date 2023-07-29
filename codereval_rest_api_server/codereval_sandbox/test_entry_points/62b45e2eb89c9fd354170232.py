"""
62b45e2eb89c9fd354170232
zimeon/ocfl-py
ocfl/object_utils.py
next_version
57
73


Given next version identifier following existing pattern

"""
import sys
import traceback
import pickle

# import ...
from ocfl.object_utils import next_version


# Test Data

#
exit_code = 0

try:
    result = next_version('v1')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
