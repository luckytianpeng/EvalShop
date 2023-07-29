"""
62b89640755ee91dce50a114
pexip/os-python-dateutil
dateutil/tz/_common.py
tzname_in_python2
13
30


Change unicode output into bytestrings in Python 2

"""
import sys
import traceback
import pickle

# import ...
from dateutil.tz._common import tzname_in_python2

# Test Data
def f():
    return 'Hello'

#
exit_code = 0

try:
    result = tzname_in_python2(f)
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
