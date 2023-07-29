"""
62ece4992e6aefcf4aabbd80
burgerbecky/makeprojects
makeprojects/util.py
remove_ending_os_sep
402
425


If input list is None, return []
    Iterate over a string list and remove trailing os seperator characters.
    Each string is tested if its length is greater than one and if the last
    character is the pathname seperator.
    Returns:
    A list after removing trailing os seperator characters.

"""
import sys
import traceback
import pickle

# import ...
from unittests.test_util import TestUtil


# Test Data
# test_data = 

#
exit_code = 0

try:
    t = TestUtil()
    result = t.test_remove_ending_os_sep()
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
