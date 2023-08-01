"""
62b463283879012d1948153d
scieloorg/packtools
packtools/sps/utils/xml_utils.py
match_pubdate
269
276


For the given node, returns the first match in the pubdate_xpaths list.

"""
import sys
import traceback
import pickle

# import ...
from packtools.sps.utils.xml_utils import match_pubdate


# Test Data
test_data = '''\
<pub-date>2023-07-03</pub-date>
'''

xpaths = (
            "pub-date"
        )

#
exit_code = 0

try:
    result = match_pubdate(test_data, xpaths)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
