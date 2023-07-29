"""
62b45e21e0d4551b0392c8ed
zimeon/ocfl-py
ocfl/object_utils.py
find_path_type
105
143


Return a string indicating the type of thing at the given path

"""
import sys
import traceback
import pickle

# import ...
from ocfl.object_utils import find_path_type


# Test Data

#
exit_code = 0

try:
    result = find_path_type('./')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
