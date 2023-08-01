"""
62ece4992e6aefcf4aabbd79
witten/borgmatic
borgmatic/borg/list.py
make_find_paths
66
87


Given a sequence of path, transform all path into glob patterns. Pass through existing patterns untouched.

    Args:
        find_paths: sequence of path
    Returns:
        tuple of transformed path

"""
import sys
import traceback
import pickle

# import ...
from borgmatic.borg.list import make_find_paths


# Test Data

#
exit_code = 0

try:
    result = make_find_paths(['foo.txt', 'pp:root/somedir'])
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
