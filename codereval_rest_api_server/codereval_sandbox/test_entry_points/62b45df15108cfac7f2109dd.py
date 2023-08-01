"""
62b45df15108cfac7f2109dd
zimeon/ocfl-py
ocfl/validator.py
status_str
65
67


Return string representation with self.log.status_str, with optional prefix.

"""
import sys
import traceback
import pickle

# import ...
from ocfl.validator import Validator


# Test Data

#
exit_code = 0

try:
    v = Validator()
    result = v.status_str()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
