"""
62ece4982e6aefcf4aabbd6b
turicas/rows
rows/utils/__init__.py
subclasses
179
184


Return all subclasses of a class, recursively

"""
import sys
import traceback
import pickle

# import ...
from rows.utils import subclasses


# Test Data
class A:
    pass

class B(A):
    pass

class C(B):
    pass

#
exit_code = 0

try:
    result = subclasses(A)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
