"""
62b8d23e48ba5a41d1c3f49e
pexip/os-python-cachetools
cachetools/rr.py
popitem
27
34


Find, remove and return a random `(key, value)` pair via __choice in the class

"""
import sys
import traceback
import pickle

# import ...
from cachetools.rr import RRCache


# Test Data
c = RRCache(maxsize=7)

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
