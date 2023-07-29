"""
62b87d23d292efb640a5566b
eykd/prestoplot
src/prestoplot/_version.py
run_command
73
116


Call the given command(s).

"""
import sys
import traceback
import pickle
from pip._internal.utils.subprocess import (
    make_command,
)

# import ...
from src.prestoplot._version import run_command


# Test Data

#
exit_code = 0

try:
    # def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    result = run_command(make_command('ls'), ['-l'])
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
