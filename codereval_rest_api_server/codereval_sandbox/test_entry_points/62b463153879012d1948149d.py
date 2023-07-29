"""
62b463153879012d1948149d
scieloorg/packtools
packtools/sps/models/packages.py
_explore_folder
147
167


Groups files in the given group by using _group_files_by_xml_filename.

"""
import sys
import traceback
import pickle

# import ...
from packtools.sps.models.packages import _explore_folder


# Test Data

#
exit_code = 0

try:
    result = _explore_folder('tests/samples')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
