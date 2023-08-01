"""
62b8d24048ba5a41d1c3f49f
pexip/os-python-cachetools
cachetools/func.py
ttl_cache
166
176


Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.

"""
import sys
import traceback
import pickle

# import ...
from cachetools.func import ttl_cache


# Test Data
@ttl_cache()
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
