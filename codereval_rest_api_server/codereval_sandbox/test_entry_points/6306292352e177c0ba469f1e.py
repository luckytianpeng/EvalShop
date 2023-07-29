"""
6306292352e177c0ba469f1e
jaywink/federation
federation/utils/text.py
process_text_links
96
116


Process links in text, adding some attributes and linkifying textual links.

"""
import sys
import traceback
import pickle

# import ...
from federation.tests.utils.test_text import TestProcessTextLinks


# Test Data

#
exit_code = 0

try:
    t = TestProcessTextLinks()
    pub_m = [m for m in dir(TestProcessTextLinks)
            if callable(getattr(t, m)) if not m.startswith('_')]
    for m in pub_m:
        getattr(t, m)()
    result = None
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
