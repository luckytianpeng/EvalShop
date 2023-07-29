"""
62b8b99de0d34b282c1811f8
champax/pysolbase
pysolbase/SolBase.py
_reset_logging
596
626


Reset the logging system

"""
import sys
import traceback
import pickle
import logging

# import ...
from pysolbase.SolBase import SolBase


# Test Data
# test_data = 

#
exit_code = 0

try:
    result = SolBase._reset_logging(log_level="DEBUG")
    assert logging.getLevelName(logging.getLogger().getEffectiveLevel())\
            == "DEBUG"

    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
