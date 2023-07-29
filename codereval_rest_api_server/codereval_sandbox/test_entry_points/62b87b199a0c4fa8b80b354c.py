"""
62b87b199a0c4fa8b80b354c
ynikitenko/lena
lena/core/split.py
_get_seq_with_type
14
66


Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).

"""
import sys
import traceback
import pickle

# import ...
from lena.core.split import _get_seq_with_type
from tests.example_sequences import (ASCIILowercase, ASCIIUppercase,
    ascii_lowercase, ascii_uppercase, lowercase_cached_filename, lowercase_cached_seq, id_)


# Test Data
test_data = [((), ()),]

#
exit_code = 0

try:
    result = _get_seq_with_type(ascii_lowercase)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
