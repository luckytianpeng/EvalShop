"""
630629e152e177c0ba46a0d1
jaywink/federation
federation/utils/network.py
try_retrieve_webfinger_document
218
232


Try to retrieve an RFC7033 webfinger document. Does not raise if it fails.

"""
import sys
import traceback
import pickle

# import ...
from federation.utils.network import try_retrieve_webfinger_document


# Test Data
test_data = "bob@localhost"

#
exit_code = 0

try:
    result = try_retrieve_webfinger_document(test_data)
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
