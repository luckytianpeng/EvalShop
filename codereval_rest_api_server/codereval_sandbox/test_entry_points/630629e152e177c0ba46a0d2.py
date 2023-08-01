"""
630629e152e177c0ba46a0d2
jaywink/federation
federation/utils/diaspora.py
retrieve_and_parse_diaspora_webfinger
71
89


Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict

"""
import sys
import traceback
import pickle

# import ...
from federation.utils.diaspora import retrieve_and_parse_diaspora_webfinger


# Test Data
test_data = "bob@localhost"

#
exit_code = 0

try:
    result = retrieve_and_parse_diaspora_webfinger(test_data)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
