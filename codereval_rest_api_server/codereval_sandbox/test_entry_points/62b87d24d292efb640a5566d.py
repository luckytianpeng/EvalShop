"""
62b87d24d292efb640a5566d
eykd/prestoplot
src/prestoplot/_version.py
plus_or_dot
383
387


Return "." If the closet-tag of the pieces contains "+", otherwise, return "+".

"""
import sys
import traceback
import pickle

# import ...
from src.prestoplot._version import plus_or_dot


# Test Data
pieces = {
    'error': False,
    'closest-tag': 'closest-tag',
    'distance': True,
    'dirty': True,
    'short': 'short',
    'long': 'long',
}

#
exit_code = 0

try:
    result = plus_or_dot(pieces)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
