"""
62b8d22a48ba5a41d1c3f47d
pexip/os-python-cachetools
cachetools/cache.py
pop
87
95


D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.

"""
import sys
import traceback
import pickle

# import ...
from cachetools.cache import Cache


# Test Data
c = Cache(maxsize=7)

c[1] = '1'
c['2'] = 2

#
exit_code = 0

try:
    result = c.pop('2')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
