"""
62b8d23c48ba5a41d1c3f49b
pexip/os-python-cachetools
cachetools/mru.py
popitem
27
34


"Remove and return the (key, value) pair most recently used.

"""
import sys
import traceback
import pickle

# import ...
from cachetools.mru import MRUCache


# Test Data
c = MRUCache(maxsize=7)

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
