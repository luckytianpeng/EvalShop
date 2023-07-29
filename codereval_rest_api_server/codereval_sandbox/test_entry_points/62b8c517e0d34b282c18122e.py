"""
62b8c517e0d34b282c18122e
champax/pysolbase
pysolbase/SolBase.py
extostr
285
381


Format the exception as a string

"""
import sys
import traceback
import pickle

# import ...
from pysolbase.SolBase import SolBase

# Test Data
# test_data = 

#
exit_code = 0

try:
    try:
        0 / 0
    except Exception as e:
        result = SolBase.extostr(e)
        # print(result)
        print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
