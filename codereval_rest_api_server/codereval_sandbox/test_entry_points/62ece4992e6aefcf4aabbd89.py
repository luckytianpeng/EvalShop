"""
62ece4992e6aefcf4aabbd89
ufo-kit/concert
concert/tests/unit/devices/test_monochromator.py
gaussian
87
93


Calculate Gaussian centered with u is 0.2 and sigma is 0.1.

"""
import sys
import traceback
import pickle

# import ...
from concert.tests.unit.devices.test_monochromator import TestDummyDoubleMonochromator


# Test Data

#
exit_code = 0

try:
    t = TestDummyDoubleMonochromator()
    result = t.gaussian(1)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
