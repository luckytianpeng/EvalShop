"""
6306292652e177c0ba469f34
jaywink/federation
federation/utils/network.py
fetch_content_type
26
35


Set the head of the request through the URL and USER_AGENT.

"""
import sys
import traceback
import pickle

# import ...
from federation.utils.network import fetch_content_type


# Test Data
test_data = {
        'https://github.com/',
        }

#
exit_code = 0

try:
    result = {}
    for i in test_data:
        result[i] = fetch_content_type(i)
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
