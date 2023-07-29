"""
62b87b4f9a0c4fa8b80b3580
ynikitenko/lena
lena/structures/hist_functions.py
integral
438
455


Calculate the area of the overall graph.

"""
import sys
import traceback
import pickle

# import ...
from lena.structures.hist_functions import integral
from tests.structures.test_histogram import test_histogram_3d


# Test Data

#
exit_code = 0

try:
    result = test_histogram_3d()
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
