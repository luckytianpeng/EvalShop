"""
62b4567ad7d32e5b55cc83af
witten/atticmatic
borgmatic/commands/generate_config.py
parse_arguments
9
35


Given command-line arguments with which this script was invoked, parse the arguments and return  them as an ArgumentParser instance

"""
import sys
import traceback
import pickle

# import ...
from borgmatic.commands.generate_config import parse_arguments


# Test Data

#
exit_code = 0

try:
    result = parse_arguments('--source', 'source.yaml', '--destination', 'config.yaml')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
