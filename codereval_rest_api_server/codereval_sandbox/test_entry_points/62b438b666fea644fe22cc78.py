"""
62b438b666fea644fe22cc78
witten/borgmatic
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
from tests.integration.commands.test_generate_config import test_parse_arguments_parses_source


# Test Data

#
exit_code = 0

try:
    result = test_parse_arguments_parses_source()
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
