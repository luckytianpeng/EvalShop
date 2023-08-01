"""
62b87b519a0c4fa8b80b3583
ynikitenko/lena
lena/structures/graph.py
scale
192
268


Get or set the scale of the graph.

If *other* is ``None``, return the scale of this graph.

If a numeric *other* is provided, rescale to that value.
If the graph has unknown or zero scale,
rescaling that will raise :exc:`~.LenaValueError`.

To get meaningful results, graph's fields are used.
Only the last coordinate is rescaled.
For example, if the graph has *x* and *y* coordinates,
then *y* will be rescaled, and for a 3-dimensional graph
*z* will be rescaled.
All errors are rescaled together with their coordinate.

"""
import sys
import traceback
import pickle

# import ...
from lena.structures.graph import graph


# Test Data
# test_data = 

#
exit_code = 0

try:
    g = graph([[0, 1], [4, 6]],
            field_names=('x', 'y'), scale=None)
    result = g.scale()
    # print(result)
    # print(g)
    print(pickle.dumps(g))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
