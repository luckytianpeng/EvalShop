"""
630629e752e177c0ba46a0fb
jaywink/federation
federation/utils/network.py
send_document
184
215


Send a response containing data through the POST method.

"""
import sys
import traceback
import pickle

# import ...
from federation.utils.network import send_document


# Test Data

#
exit_code = 0

try:
    result = send_document("http://localhost", {"foo": "bar"})
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
