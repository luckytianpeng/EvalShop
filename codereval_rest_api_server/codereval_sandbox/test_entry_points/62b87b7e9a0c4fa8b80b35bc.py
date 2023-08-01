"""
62b87b7e9a0c4fa8b80b35bc
ynikitenko/lena
lena/structures/graph.py
_update_context
315
359


Update *context* with the properties of this graph.

*context.error* is appended with indices of errors.
Example subcontext for a graph with fields "E,t,error_E_low":
{"error": {"x_low": {"index": 2}}}.
Note that error names are called "x", "y" and "z"
(this corresponds to first three coordinates,
if they are present), which allows to simplify plotting.
Existing values are not removed
from *context.value* and its subcontexts.

Called on "destruction" of the graph (for example,
in :class:`.ToCSV`). By destruction we mean conversion
to another structure (like text) in the flow.
The graph object is not really destroyed in this process.

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
    result = g._update_context('x')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
