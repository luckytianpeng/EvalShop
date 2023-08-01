"""
62b8d23b48ba5a41d1c3f49a
pexip/os-python-cachetools
cachetools/func.py
mru_cache
139
149


Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
algorithm.

"""
import sys
import traceback
import pickle

# import ...
from cachetools.func import mru_cache


# Test Data
@mru_cache()
def f():
    pass

#
exit_code = 0

try:
    f()
    result = dir(f)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
