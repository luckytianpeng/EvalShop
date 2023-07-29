"""
62b8982f755ee91dce50a241
pexip/os-python-dateutil
dateutil/relativedelta.py
normalized
282
315


Normalize all units of time to integers.

"""
import sys
import traceback
import pickle

# import ...
from dateutil.relativedelta import relativedelta


# Test Data


#
exit_code = 0

try:
    rel = relativedelta()
    result = rel.normalized()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
