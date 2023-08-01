"""
62b8d22948ba5a41d1c3f47c
pexip/os-python-cachetools
cachetools/cache.py
get
81
85


If a key exists in the class, the value corresponding to the key is returned. Otherwise, default is returned.

"""
import sys
import traceback
import pickle

# import ...
from cachetools.cache import Cache


# Test Data
cache = Cache(maxsize=2)

cache[1] = 'a'
cache[2] = 'b'
cache[3] = 'c'

#
exit_code = 0

try:
    result = cache.get(2)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
