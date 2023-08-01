"""
62b463153879012d1948149b
scieloorg/packtools
packtools/sps/models/packages.py
match_file_by_prefix
113
135


Given a filepath, return true if the basename of the filepath is startswith the given prefix plus "-" or the given prefix plus "."

"""
import sys
import traceback
import pickle

# import ...
from packtools.sps.models.packages import match_file_by_prefix


# Test Data

#
exit_code = 0

try:
    result = match_file_by_prefix('_test_79', '_test_79.py')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
