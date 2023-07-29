"""
62b8d23948ba5a41d1c3f498
pexip/os-python-cachetools
cachetools/func.py
lru_cache
125
136


Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.

"""
import sys
import traceback
import pickle

# import ...
from cachetools.func import lru_cache


# Test Data
@lru_cache()
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
