"""
62b87b839a0c4fa8b80b35cb
ynikitenko/lena
lena/structures/graph.py
_get_err_indices
173
180


Find all error indexes corresponding to coord_name.

"""
import sys
import traceback
import pickle

# import ...
from lena.structures.graph import graph


# Test Data

#
exit_code = 0

try:
    g = graph([[0, 1], [4, 6]],
            field_names=('x', 'y'), scale=None)
    result = g._get_err_indices('x')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
