"""
62b4631b3879012d194814dd
scieloorg/packtools
packtools/sps/utils/xml_utils.py
fix_namespace_prefix_w
59
70


Replace "w:st=" in content with "w-st=".

"""
import sys
import traceback
import pickle

# import ...
from packtools.sps.utils.xml_utils import fix_namespace_prefix_w


# Test Data
test_data = '''\
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
<here>w:st="</here>
</note>
'''

#
exit_code = 0

try:
    result = fix_namespace_prefix_w(test_data)
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
