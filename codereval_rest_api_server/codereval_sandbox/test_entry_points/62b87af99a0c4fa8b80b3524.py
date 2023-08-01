"""
62b87af99a0c4fa8b80b3524
ynikitenko/lena
lena/core/check_sequence_type.py
is_run_el
57
59


Check whether the obj class has the run method.

"""
import sys
import traceback
import pickle

# import ...
from lena.core.check_sequence_type import is_run_el


# Test Data
test_data = {}

#
exit_code = 0

try:
    result = is_run_el(test_data)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
