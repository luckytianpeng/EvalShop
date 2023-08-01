"""
62b8d22a48ba5a41d1c3f47e
pexip/os-python-cachetools
cachetools/cache.py
setdefault
97
102


If a key exists in the class, the value corresponding to the key is returned. Otherwise, the value corresponding to the key is set to default.

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
    result = cache.setdefault(key=3)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
