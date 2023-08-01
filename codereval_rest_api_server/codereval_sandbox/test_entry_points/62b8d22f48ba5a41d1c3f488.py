"""
62b8d22f48ba5a41d1c3f488
pexip/os-python-cachetools
cachetools/fifo.py
popitem
24
31


Remove the value corresponding to the first inserted key and returns the key and value in tuple format.

"""
import sys
import traceback
import pickle

# import ...
from cachetools.fifo import FIFOCache


# Test Data
cache = FIFOCache(maxsize=2)

cache[1] = 1
cache[2] = 2
cache[3] = 3
#
exit_code = 0

try:
    result = cache.popitem()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
