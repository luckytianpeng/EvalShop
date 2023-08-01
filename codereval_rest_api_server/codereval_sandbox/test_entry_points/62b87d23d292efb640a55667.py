"""
62b87d23d292efb640a55667
eykd/prestoplot
src/prestoplot/_version.py
register_vcs_handler
60
70


Create decorator to mark a method as the handler of a object

"""
import sys
import traceback
import pickle

# import ...
from src.prestoplot._version import HANDLERS, register_vcs_handler

# Test Data
@register_vcs_handler("myapp", "myfunction")
def f():
    pass

#
exit_code = 0

try:
    # print(HANDLERS)
    print(pickle.dumps(HANDLERS))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
