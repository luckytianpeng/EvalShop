"""
62b8d23a48ba5a41d1c3f499
pexip/os-python-cachetools
cachetools/lru.py
popitem
27
34


Remove and return the `(key, value)` pair least recently used.

"""
import sys
import traceback
import pickle

# import ...
from cachetools.lru import LRUCache


# Test Data
c = LRUCache(maxsize=7)

c[1] = 1
c[2] = 2
c[3] = 3

#
exit_code = 0

try:
    result = c.popitem()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
