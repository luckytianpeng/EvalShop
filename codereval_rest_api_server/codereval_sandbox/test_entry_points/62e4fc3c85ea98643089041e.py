"""
62e4fc3c85ea98643089041e
pre-commit/pre-commit
pre_commit/languages/r.py
_inline_r_setup
146
155


Some behaviour of R cannot be configured via env variables, but can
only be configured via R options once R has started. These are set here.

"""
import sys
import traceback
import pickle

# import ...
from pre_commit.languages.r import _inline_r_setup


# Test Data
test_data = 'configure option'

#
exit_code = 0

try:
    result = _inline_r_setup(test_data)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
