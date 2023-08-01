"""
62e4fbda85ea986430890405
pre-commit/pre-commit
pre_commit/xargs.py
xargs
116
168


Simplified Implementation of Xargs in Linux

"""
import sys
import traceback
import pickle

# import ...
from pre_commit.xargs import xargs


# Test Data

#
exit_code = 0

try:
    result = xargs(('git', '--version'), [])
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
