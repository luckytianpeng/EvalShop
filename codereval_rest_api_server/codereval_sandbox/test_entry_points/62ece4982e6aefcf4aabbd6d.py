"""
62ece4982e6aefcf4aabbd6d
skorokithakis/shortuuid
shortuuid/main.py
string_to_int
29
39


Convert a string to a number, using the given alphabet.
    :param string: a string consist of the letters in alphabet
    :param alphabet: list of letters
    :return: int, the corresponding number of the given string using the given transition rule.

"""
import sys
import traceback
import pickle

# import ...
from shortuuid.main import int_to_string, string_to_int


# Test Data
number = 12345
alphabet = 'WXYZ'
string = 'ZWWWZYX'

#
exit_code = 0

try:
    result = string_to_int(string, alphabet)
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
