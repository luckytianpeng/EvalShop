"""
62ece4982e6aefcf4aabbd68
skorokithakis/shortuuid
shortuuid/main.py
int_to_string
10
26


Convert a number to a string, using the given alphabet.
    The number represents a short uuid.
    The output has the most significant digit first.
    @param number: Int value
    @param alphabet : List with letters
    @param padding : Optional with int value
    @return  string value corresponded to int

"""
import sys
import traceback
import pickle

# import ...
from shortuuid.main import int_to_string


# Test Data

#
exit_code = 0

try:
    result = int_to_string(12345, 'WXYZ')
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
