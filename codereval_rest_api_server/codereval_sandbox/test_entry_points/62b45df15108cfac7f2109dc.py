"""
62b45df15108cfac7f2109dc
zimeon/ocfl-py
ocfl/validation_logger.py
status_str
79
84


Return a string with visiting the sorted self.messages list, each visit add prefix and the element in the sorted self.messages list.

"""
import sys
import traceback
import pickle

# import ...
from ocfl.validation_logger import ValidationLogger
from tests.test_validation_logger import TestAll

# Test Data

#
exit_code = 0

try:
    t = TestAll()
    result = t.test_init()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
