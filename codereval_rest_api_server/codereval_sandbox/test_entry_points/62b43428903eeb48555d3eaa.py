"""
62b43428903eeb48555d3eaa
cpburnz/python-sql-parameters
sqlparams/__init__.py
formatmany
524
580


Convert sql using self._converter.convert_many

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
    result = t.test_2_format_bytes_many()
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
