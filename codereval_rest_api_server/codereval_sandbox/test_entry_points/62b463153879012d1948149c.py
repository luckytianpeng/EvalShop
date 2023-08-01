"""
62b463153879012d1948149c
scieloorg/packtools
packtools/sps/models/packages.py
select_filenames_by_prefix
89
110


For each file in files, return all files taht match the given prefix

"""
import sys
import traceback
import pickle

# import ...
from packtools.sps.models.packages import select_filenames_by_prefix


# Test Data

#
exit_code = 0

try:
    result = select_filenames_by_prefix('_test_79', '_test_79.py')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
