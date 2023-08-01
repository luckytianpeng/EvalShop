"""
6306292052e177c0ba469f09
jaywink/federation
federation/protocols/diaspora/protocol.py
identify_request
33
52


Check whether the request body loaded using JSON contains events. If yes, True is returned, otherwise, check whether the tag of the XML loaded from the request body is Magic_ENV_TAG, if yes, return True. If neither of the preceding conditions is met, return False.

"""
import sys
import traceback
import pickle

# import ...
# from federation.protocols.diaspora.protocol import identify_request
from federation.tests.protocols.diaspora.test_protocol import TestDiasporaProtocol



# Test Data
# test_data = 

#
exit_code = 0

try:
    t = TestDiasporaProtocol()
    t.test_identify_payload_with_diaspora_public_payload()
    t.test_identify_payload_with_diaspora_encrypted_payload()
    t.test_identify_payload_with_other_payload()
    t.test_identify_payload_with_reshare()
    result = None
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
