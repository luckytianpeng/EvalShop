"""
62b87af09a0c4fa8b80b34f1
ynikitenko/lena
lena/structures/histogram.py
fill
157
182


Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.

"""
import sys
import traceback
import pickle

# import ...
from lena.structures.histogram import histogram


# Test Data
test_data = [0, 1, 2]

#
exit_code = 0

try:
    h = histogram([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    result = h.fill(test_data)
    # print(result)
    # print(test_data)
    # print(h)
    print(pickle.dumps(h))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
