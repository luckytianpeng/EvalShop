"""
62b8d27a48ba5a41d1c3f4c6
pexip/os-python-cachetools
cachetools/decorators.py
cached
6
44


Returns a decorator function that saves the results in the cache

"""
import sys
import traceback
import pickle

# import ...
from cachetools.decorators import cached


# Test Data
cache = {}
@cached(cache)
def f(name, title='Mr.', works=[]):
    pass

#
exit_code = 0

try:
    f('Issac Newton', 'Sir', 'Mathematical Principles of Natural Philosophy')
    result = cache
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
