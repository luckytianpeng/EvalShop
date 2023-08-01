"""
62ece4982e6aefcf4aabbd66
burgerbecky/makeprojects
makeprojects/util.py
was_processed
430
459


Check if a file or directory has already been processed.

    To prevent recursion, expand the path name to an absolution path
    call this function with a set that will store all the entries and
    the entry to test. If the entry is already in the set, report the issue
    and return ``True``. Otherwise, add the entry to the set and return
    ``False`` to allow the path to be processed.

    Args:
        processed: Set to store processed pathnames
        path_name: Path to a directory or file
        verbose: True if verbose output is requested

    Returns:
        True if it's already in the set. False if not.

"""
import sys
import traceback
import pickle

# import ...
# from makeprojects.util
from unittests.test_util import TestUtil


# Test Data
# test_data = 

#
exit_code = 0

try:
    # result = test_function(test_data)
    t = TestUtil()
    result = t.test_was_processed()
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
