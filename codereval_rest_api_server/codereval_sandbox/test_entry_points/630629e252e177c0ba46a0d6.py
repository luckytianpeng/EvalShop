"""
630629e252e177c0ba46a0d6
jaywink/federation
federation/utils/diaspora.py
retrieve_diaspora_host_meta
92
103


Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance

"""
import sys
import traceback
import pickle

# import ...
from federation.utils.diaspora import retrieve_diaspora_host_meta


# Test Data
test_data = 'localhost'

#
exit_code = 0

try:
    result = retrieve_diaspora_host_meta(test_data)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
