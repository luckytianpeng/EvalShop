"""
62ece4982e6aefcf4aabbd5f
infobloxopen/infoblox-client
infoblox_client/utils.py
paging
120
133


Return every response with the length of max_results
    Args:
    response (list): WAPI response.
    max_results (int): Maximum number of objects to be returned in one page.
    Returns:
        Generator object with WAPI response split page by page.

"""
import sys
import traceback
import pickle

# import ...
# from infoblox_client.utils import paging
from tests.test_utils import TestUtils


# Test Data

#
exit_code = 0

try:
    t = TestUtils()
    result = t.test_paging()
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
