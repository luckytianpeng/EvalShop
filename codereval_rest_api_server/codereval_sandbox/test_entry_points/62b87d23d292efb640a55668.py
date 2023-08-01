"""
62b87d23d292efb640a55668
eykd/prestoplot
src/prestoplot/_version.py
get_config
38
49


Return a new VersioneerConfig() and set various attribute of it.

"""
import sys
import traceback
import pickle

# import ...
from src.prestoplot._version import get_config


# Test Data

#
exit_code = 0

try:
    result = get_config()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
