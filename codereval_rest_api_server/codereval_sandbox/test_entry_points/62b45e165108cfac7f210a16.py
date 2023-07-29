"""
62b45e165108cfac7f210a16
zimeon/ocfl-py
ocfl/inventory_validator.py
validate_as_prior_version
463
507


Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.

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
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
