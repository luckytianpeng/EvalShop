"""
62b45e145108cfac7f210a09
zimeon/ocfl-py
ocfl/inventory_validator.py
check_digests_present_and_used
396
405


Check all digests in manifest that are needed are present and used. Return error() in the class.

"""
import sys
import traceback
import pickle

# import ...
from ocfl.inventory_validator import InventoryValidator
from tests.test_inventory_validator import TestAll

# Test Data

#
exit_code = 0

try:
    t = TestAll()
    result = t.test_check_digests_present_and_used()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
