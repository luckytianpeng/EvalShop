"""
62b45e23e0d4551b0392c90a
zimeon/ocfl-py
ocfl/validator.py
validate_version_inventories
234
325


Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).

"""
import sys
import traceback
import pickle

# import ...


# Test Data
test_data = 

#
exit_code = 0

try:
    result = test_function(test_data)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
