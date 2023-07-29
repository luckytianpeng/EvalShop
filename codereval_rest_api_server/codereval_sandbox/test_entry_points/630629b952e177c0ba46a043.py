"""
630629b952e177c0ba46a043
jaywink/federation
federation/hostmeta/generators.py
get_nodeinfo_well_known_document
314
332


Returns a formatted dictionary, including information such as url and document_path.

"""
import sys
import traceback
import pickle

# import ...
from federation.tests.hostmeta.test_generators import TestNodeInfoGenerator


# Test Data

#
exit_code = 0

try:
    t = TestNodeInfoGenerator()
    result = t.test_nodeinfo_wellknown_document()
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
