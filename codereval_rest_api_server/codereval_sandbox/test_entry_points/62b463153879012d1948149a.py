"""
62b463153879012d1948149a
scieloorg/packtools
packtools/sps/models/packages.py
_group_files_by_xml_filename
194
239


Groups files by xmls and returns data in dict format.

"""
import sys
import traceback
import pickle

# import ...
# from packtools.sps.models.packages import _group_files_by_xml_filename
from tests.sps.test_packages import Test_group_files_by_xml_filename

# Test Data

#
exit_code = 0

try:
    t = Test_group_files_by_xml_filename()
    result = t.test__group_files_by_xml_filename()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
