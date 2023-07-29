"""
6306292352e177c0ba469f1d
jaywink/federation
federation/utils/text.py
find_tags
25
85


Find tags in text.

Tries to ignore tags inside code blocks.

Optionally, if passed a "replacer", will also replace the tag word with the result
of the replacer function called with the tag word.

Returns a set of tags and the original or replaced text.

"""
import sys
import traceback
import pickle

# import ...
from federation.tests.utils.test_text import TestFindTags


# Test Data

#
exit_code = 0

try:
    t = TestFindTags()
    result = t.test_finds_tags()
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
