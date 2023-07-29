"""
62b45e165108cfac7f210a17
zimeon/ocfl-py
ocfl/inventory_validator.py
get_logical_path_map
13
28


Returns the file paths of the states in the inventory in the dict type.

"""
import sys
import traceback
import pickle

# import ...
from tests.test_inventory_validator import TestAll


# Test Data 

#
exit_code = 0

try:
    t = TestAll()
    result = t.test_validate_as_prior_version()
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
