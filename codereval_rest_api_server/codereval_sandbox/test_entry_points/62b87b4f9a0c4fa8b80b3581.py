"""
62b87b4f9a0c4fa8b80b3581
ynikitenko/lena
lena/structures/histogram.py
scale
187
222


Compute or set scale (integral of the histogram).

If *other* is ``None``, return scale of this histogram.
If its scale was not computed before,
it is computed and stored for subsequent use
(unless explicitly asked to *recompute*).
Note that after changing (filling) the histogram
one must explicitly recompute the scale
if it was computed before.

If a float *other* is provided, rescale self to *other*.

Histograms with scale equal to zero can't be rescaled.
:exc:`.LenaValueError` is raised if one tries to do that.

"""
import sys
import traceback
import pickle

# import ...
from lena.structures.histogram import histogram


# Test Data

#
exit_code = 0

try:
    h = histogram([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    result = h.scale()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
