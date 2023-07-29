"""
62b87af19a0c4fa8b80b34f7
ynikitenko/lena
lena/context/functions.py
difference
58
94


Return a dictionary with items from d1 not contained in d2.

"""
import sys
import traceback
import pickle

# import ...
from lena.context.functions import difference


# Test Data
d1 = {
    'level01': {
        'level02': True
    }
}
d2 = {
    'level01': {
        'level02': False
    }
}

#
exit_code = 0

try:
    result = difference(d1, d2, 3)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
