"""
62b463153879012d19481498
scieloorg/packtools
packtools/file_utils.py
files_list
28
32


Return the files in given path.

"""
import sys
import traceback
import pickle

# import ...
from packtools.file_utils import files_list


# Test Data

#
exit_code = 0

try:
    result = files_list('.')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
