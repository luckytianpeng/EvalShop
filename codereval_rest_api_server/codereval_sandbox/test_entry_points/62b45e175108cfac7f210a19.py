"""
62b45e175108cfac7f210a19
zimeon/ocfl-py
ocfl/inventory_validator.py
validate_fixity
192
238


Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.

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
    result = t.test_validate_fixity()
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
