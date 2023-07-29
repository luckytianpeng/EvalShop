"""
62b43427903eeb48555d3ea5
cpburnz/python-sql-parameters
sqlparams/__init__.py
format
472
522


Convert sql using self._converter.convert

"""
import sys
import traceback
import pickle

# import ...
from tests.test_1_general import Test


# Test Data
# test_data = 

#
exit_code = 0

try:
    t = Test()
    result = t.test_2_format_bytes()
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
