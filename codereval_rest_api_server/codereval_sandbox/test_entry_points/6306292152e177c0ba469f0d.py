"""
6306292152e177c0ba469f0d
jaywink/federation
federation/protocols/matrix/protocol.py
identify_request
24
35


Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.

"""
import sys
import traceback
import pickle

# import ...
from federation.tests.protocols.matrix.test_protocol import TestIdentifyRequest


# Test Data

#
exit_code = 0

try:
    t = TestIdentifyRequest()
    t.test_identifies_matrix_request()
    t.test_passes_gracefully_for_non_matrix_request()
    result = None
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
