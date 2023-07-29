"""
62ece4982e6aefcf4aabbd77
witten/borgmatic
borgmatic/borg/check.py
parse_frequency
53
89


Given a frequency string with a number and a unit of time, return a corresponding
     datetime.timedelta instance.
     If the frequency is None or "always", return None.
     Raise ValueError if the given frequency cannot be parsed.
     For instance, given "3 timeunit", return datetime.timedelta(timeunit=3)

     @param frequency :  A frequency string "number timeunit"

    @return str, the corresponding datetime

"""
import sys
import traceback
import pickle

# import ...
from borgmatic.borg.check import parse_frequency
from tests.unit.borg.test_check import test_parse_frequency_parses_into_timedeltas


# Test Data

#
exit_code = 0

try:
    result = parse_frequency('3 weeks')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
