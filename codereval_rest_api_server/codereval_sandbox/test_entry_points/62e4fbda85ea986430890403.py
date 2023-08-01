"""
62e4fbda85ea986430890403
pre-commit/pre-commit
pre_commit/languages/helpers.py
_shuffled
111
118


Shuffle a given seq with the given FIXED_RANDOM_SEED

"""
import sys
import traceback
import pickle

# import ...
from pre_commit.languages.helpers import _shuffled


# Test Data
test_data = ['a', 'b', 'c', 'd']

#
exit_code = 0

try:
    result = _shuffled(test_data)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
