"""
62b87b199a0c4fa8b80b354e
ynikitenko/lena
lena/core/check_sequence_type.py
is_fill_request_seq
40
54


Check whether seq can be converted to FillRequestSeq and bool is returned.

"""
import sys
import traceback
import pickle

# import ...
from lena.core.check_sequence_type import is_fill_request_seq


# Test Data
test_data = {}

#
exit_code = 0

try:
    result = is_fill_request_seq(test_data)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
