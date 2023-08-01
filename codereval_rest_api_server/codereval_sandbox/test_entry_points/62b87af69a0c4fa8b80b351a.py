"""
62b87af69a0c4fa8b80b351a
ynikitenko/lena
lena/core/check_sequence_type.py
is_fill_compute_el
6
11


Check whether the obj class has the fill and compute methods.

"""
import sys
import traceback
import pickle

# import ...
from lena.core.check_sequence_type import is_fill_compute_el


# Test Data
test_data = {}

#
exit_code = 0

try:
    result = is_fill_compute_el(test_data)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
