"""
62b45665d7d32e5b55cc8365
witten/atticmatic
borgmatic/commands/arguments.py
parse_arguments
1109
1180


Parses parameters and returns them as dict maps

"""
import sys
import traceback
import pickle

# import ...
# from borgmatic.commands import arguments as module
from borgmatic.commands.arguments import parse_arguments


# Test Data

#
exit_code = 0

try:
    result = parse_arguments('--config', 'myconfig', 'extract', '--archive', 'test')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
