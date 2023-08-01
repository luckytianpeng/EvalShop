"""
62e5dc9ed76274f8a4026b5b
neo4j/neo4j-python-driver
src/neo4j/_meta.py
deprecated
91
101


Return a decorator function for deprecating functions and methods.

"""
import sys
import traceback
import pickle

# import ...
from src.neo4j._meta import deprecated


# Test Data
# test_data = 

@deprecated("'foo' has been deprecated in favour of 'bar'")
def foo(x):
    pass

#
exit_code = 0

try:
    # result = deprecated("'foo' has been deprecated in favour of 'bar'")
    result = dir(foo)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
