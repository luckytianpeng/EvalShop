"""
62ece4982e6aefcf4aabbd64
zimeon/ocfl-py
ocfl/dispositor.py
strip_root
10
15


Remove root from path. If fails, throw exception

    Returns:
        A path without root

"""
import sys
import traceback
import pickle

# import ...
from ocfl.dispositor import Dispositor
from tests.test_dispositor import TestAll


# Test Data
#
exit_code = 0

try:
    t = TestAll()
    result = t.test01_almost_everything()
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
