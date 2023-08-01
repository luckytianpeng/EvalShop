"""
630629d052e177c0ba46a0a1
jaywink/federation
federation/protocols/diaspora/signatures.py
verify_relayable_signature
30
37


Verify the signed XML elements to have confidence that the claimed
author did actually generate this message.

"""
import sys
import traceback
import pickle

# import ...
from federation.tests.protocols.diaspora.test_signatures import test_verify_relayable_signature


# Test Data

#
exit_code = 0

try:
    result = test_verify_relayable_signature()
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
