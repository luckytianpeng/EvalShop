"""
6305f9991d275c6667163c50
MozillaSecurity/lithium
src/lithium/testcases.py
set_cut_chars
371
391


Set the bytes used to delimit slice points.

Args:
    before: Split file before these delimiters.
    after: Split file after these delimiters.

"""
import sys
import traceback
import pickle

# import ...
from src.lithium.testcases import TestcaseSymbol

# Test Data
# test_data = 

#
exit_code = 0

try:
    t = TestcaseSymbol()
    result = t._cutter
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
