"""
62b8d23748ba5a41d1c3f496
pexip/os-python-cachetools
cachetools/func.py
lfu_cache
111
122


Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.

"""
import sys
import traceback
import pickle

# import ...
from cachetools.func import lfu_cache


# Test Data
@lfu_cache()
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
