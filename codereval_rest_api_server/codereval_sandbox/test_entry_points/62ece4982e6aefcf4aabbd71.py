"""
62ece4982e6aefcf4aabbd71
burgerbecky/makeprojects
makeprojects/util.py
regex_dict
72
98


Convert *.cpp keys to regex keys.
Given a dict where the keys are all filenames with wildcards,
convert only the keys into equivalent regexes and leave the values intact.

Args:
    item: dict to convert
Returns:
    dict with keys converted to regexes

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
    result = t.test_regex_dict()
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
