"""
62b45e145108cfac7f210a07
zimeon/ocfl-py
ocfl/inventory_validator.py
validate
62
144


Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)

"""
import sys
import traceback
import pickle

# import ...
from ocfl.inventory_validator import InventoryValidator


# Test Data

#
exit_code = 0

try:
    i = InventoryValidator()
    result = i.validate([])
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
