"""
62b463163879012d194814a4
scieloorg/packtools
packtools/sps/models/packages.py
_explore_zipfile
170
191


Groups the given zip path by using _group_files_by_xml_filename.

"""
import sys
import traceback
import pickle

# import ...
from tests.sps.test_packages import TestZipFile


# Test Data

#
exit_code = 0

try:
    t = TestZipFile()
    result = t.test_explore_zipfile_returns_zip_data()
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
