"""
62b87d24d292efb640a55670
eykd/prestoplot
src/prestoplot/_version.py
get_versions
637
686


Obtains the version information. If the version information cannot be obtained, the default value is returned.

"""
import sys
import traceback
import pickle

# import ...
from src.prestoplot._version import get_versions


# Test Data

#
exit_code = 0

try:
    result = get_versions()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
