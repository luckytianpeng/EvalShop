"""
62b463303879012d19481579
scieloorg/packtools
packtools/sps/models/front_articlemeta_issue.py
_extract_number_and_supplment_from_issue_element
19
62


Return the possible values of number and sup from the contents of issue.

"""
import sys
import traceback
import pickle

# import ...
from packtools.sps.models.front_articlemeta_issue import _extract_number_and_supplment_from_issue_element

# Test Data
#
exit_code = 0

try:
    result = _extract_number_and_supplment_from_issue_element("5 (suppl)")
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
