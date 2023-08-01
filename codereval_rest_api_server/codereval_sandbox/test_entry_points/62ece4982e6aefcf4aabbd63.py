"""
62ece4982e6aefcf4aabbd63
openstack/cinder
cinder/api/api_utils.py
is_none_string
62
67


Check if a string represents a None value.
    Returns:
        Return True if the type of val is string and the lowercase of val is equal to 'none', otherwise return False

"""
import sys
import traceback
import pickle

# import ...
from cinder.api.api_utils import is_none_string


# Test Data
test_data = ['123', 123, {'name': 'Tom'}, [1, 2], 'none', 'None', 'NONE']

#
exit_code = 0

try:
    result = []
    for i in test_data:
        result.append(is_none_string(i))
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
