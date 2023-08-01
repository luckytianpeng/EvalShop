"""
6306292a52e177c0ba469f41
jaywink/federation
federation/utils/text.py
test_tag
119
126


Checks whether each character in the LEEGAL_TAG_CHARS belongs to a tag. If any character belongs to a tag, the value False is returned. Otherwise, the value True is returned.

"""
import sys
import traceback
import pickle

# import ...
from federation.utils.text import test_tag


# Test Data
test_data = {
    'here are spaces',
    'a-normal-string',
    'https://a_url.com'
}

#
exit_code = 0

try:
    result = {}
    for i in test_data:
        result[i] = test_tag(i)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
