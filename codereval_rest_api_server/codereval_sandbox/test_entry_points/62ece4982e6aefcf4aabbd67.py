"""
62ece4982e6aefcf4aabbd67
santoshphilip/eppy
eppy/geometry/surface.py
vertex3tuple
91
105


Get 3 points for each vertex of the polygon.
    This will include the vertex and the 2 points on both sides of the vertex
    If the subscript is out of bounds, take the value of index as 0
    Args:
        vertices: vertices to be converted

    Returns:
        A list where the elements of vertices represented by tuple

"""
import sys
import traceback
import pickle

# import ...
from eppy.geometry.surface import vertex3tuple


# Test Data
test_data = (1, 2, 3, 4, )

#
exit_code = 0

try:
    result = vertex3tuple(test_data)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
