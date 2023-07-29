"""
62b463153879012d194814a1
scieloorg/packtools
packtools/sps/models/packages.py
add_rendition
49
56


Assign the filepath invoke by filepath() in the class to "lang" in _renditions in the class.

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
