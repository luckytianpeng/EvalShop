"""
62ece4982e6aefcf4aabbd72
ikus060/rdiffweb
rdiffweb/core/librdiff.py
unquote
88
103


Remove quote from the given name with regular expression.
    Args:
        name: input name
    Returns:
        name after removal

"""
import sys
import traceback
import pickle

# import ...
from rdiffweb.core.librdiff import unquote


# Test Data

#
exit_code = 0

try:
    result = unquote(f'~/data/001;002;003;004'.encode())
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
