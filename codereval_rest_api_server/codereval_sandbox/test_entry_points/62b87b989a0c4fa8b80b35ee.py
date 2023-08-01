"""
62b87b989a0c4fa8b80b35ee
ynikitenko/lena
lena/structures/histogram.py
reset
296
310


Current context is reset to an empty dict, bins of the class are reinitialized with the *initial_value* or with *make_bins()*.

"""
import sys
import traceback
import pickle

# import ...
from lena.structures import histogram, Histogram


# Test Data
hist = histogram([0, 1, 2])

# test simple initialization
# probably should make a deep copy of these bins and edges here
h0 = Histogram(hist.edges, hist.bins)

#
exit_code = 0

try:
    result = h0.reset()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
