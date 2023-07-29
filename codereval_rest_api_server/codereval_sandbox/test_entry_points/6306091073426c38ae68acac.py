"""
6306091073426c38ae68acac
redhat-openstack/infrared
infrared/core/utils/dict_utils.py
dict_insert
8
32


insert a value of a nested key into a dictionary

to insert value for a nested key, all ancestor keys should be given as
method's arguments

example:
  dict_insert({}, 'val', 'key1.key2'.split('.'))

:param dic: a dictionary object to insert the nested key value into
:param val: a value to insert to the given dictionary
:param key: first key in a chain of key that will store the value
:param keys: sub keys in the keys chain

"""
import sys
import traceback
import pickle

# import ...
from tests.test_utils import test_dict_insert

# Test Data

#
exit_code = 0

try:
    result = test_dict_insert(
            {'a_key': 'a_val', 'b_key1': {'b_key2': {'b_key3': 'b_val'}}},
            'x_val',
            ['b_key1', 'b_key2'],
            {'a_key': 'a_val', 'b_key1': {'b_key2': 'x_val'}})
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
