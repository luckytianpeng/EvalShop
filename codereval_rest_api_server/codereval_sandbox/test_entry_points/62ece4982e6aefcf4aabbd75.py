"""
62ece4982e6aefcf4aabbd75
commandline/flashbake
src/flashbake/plugins/ignored.py
addignored
37
45


Use the git command to obtain the file names。
    Turn the file names into a list, sort the list for only ignored files
    return those files as a single string with each filename separated by a comma.

"""
import sys
import traceback
import pickle

# import ...
from src.flashbake.plugins.ignored import Ignored


# Test Data
# test_data =

#
exit_code = 0

try:
    i = Ignored('something')
    result = i.addignored('./')
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
