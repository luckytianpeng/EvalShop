"""
62ece4982e6aefcf4aabbd6a
sipwise/repoapi
release_dashboard/templatetags/rd_extras.py
replace_dots
23
25


Replaces all values of '.' to arg from the given string
    Args:
        value: old string
        arg: new string to replace '.'
    Returns:
        str, the replaced string

"""
import sys
import traceback
import pickle

# import ...
from release_dashboard.templatetags.rd_extras import replace_dots


# Test Data

#
exit_code = 0

try:
    result = replace_dots('www.google.com', ' ')
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
