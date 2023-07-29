"""
62b8a4a4755ee91dce50a3d2
pexip/os-python-dateutil
dateutil/tz/_common.py
_fromutc
207
242


Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.

"""
import sys
import traceback
import pickle
from datetime import datetime

# import ...
from dateutil.tz._common import _tzinfo
from dateutil.tz import tzoffset


# Test Data
_brsttz = tzoffset("BRST", -10800)
dt = datetime(2003, 9, 25, 10, 49, 41, 500000, tzinfo=_brsttz)

#
exit_code = 0

try:
    t = _tzinfo()
    result = t._fromutc(dt)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
