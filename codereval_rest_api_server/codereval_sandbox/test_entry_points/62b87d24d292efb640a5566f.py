"""
62b87d24d292efb640a5566f
eykd/prestoplot
src/prestoplot/_version.py
render
595
634


Input pieces and a style, render the pieces to the corresponding style.

"""
import sys
import traceback
import pickle

# import ...
from src.prestoplot._version import get_versions, render


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
    result = render(pieces, 'default')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
