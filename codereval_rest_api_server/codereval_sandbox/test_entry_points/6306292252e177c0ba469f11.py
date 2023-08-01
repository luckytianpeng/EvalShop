"""
6306292252e177c0ba469f11
jaywink/federation
federation/entities/diaspora/utils.py
format_dt
16
22


Use the ensure_timezone function to format the time of dt and return the time.

"""
import sys
import traceback
import pickle

# import ...
from federation.tests.entities.diaspora.test_utils import TestFormatDt


# Test Data

#
exit_code = 0

try:
    t = TestFormatDt()
    t.test_formatted_string_returned_from_tz_aware_datetime()
    result = None
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
