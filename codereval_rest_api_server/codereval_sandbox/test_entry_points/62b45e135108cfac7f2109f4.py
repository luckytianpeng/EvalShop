"""
62b45e135108cfac7f2109f4
zimeon/ocfl-py
ocfl/dispositor.py
is_valid
17
19


Return True if identifier is valid. In this base implementation, always return True.  (D)

"""
import sys
import traceback
import pickle

# import ...
from ocfl.dispositor import Dispositor


# Test Data

#
exit_code = 0

try:
    d = Dispositor()
    result = d.is_valid(None)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
