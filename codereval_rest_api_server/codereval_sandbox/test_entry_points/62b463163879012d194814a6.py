"""
62b463163879012d194814a6
scieloorg/packtools
packtools/file_utils.py
files_list_from_zipfile
56
76


Return the files in the given zip path.

"""
import sys
import traceback
import pickle

# import ...
from packtools.file_utils import files_list_from_zipfile


# Test Data

#
exit_code = 0

try:
    result = files_list_from_zipfile('./tests/sps/fixtures/package.zip')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
