"""
62ece4982e6aefcf4aabbd62
SEED-platform/py-seed
pyseed/seed_client_base.py
_replace_url_args
41
46


Replace the value in url with the value in url_args
    If url_args has a value, iterate over the keys and values from url_args.
    Then replace the keys of the first parameter with values.
    Returns: the modified url.

"""
import sys
import traceback
import pickle

# import ...
from pyseed.seed_client_base import _replace_url_args


# Test Data
url = 'https://www.amazon.com/s?k=oxford+dictionary'
url_args = {
    'k': 'keyword'
}

#
exit_code = 0

try:
    result = _replace_url_args(url, url_args)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
