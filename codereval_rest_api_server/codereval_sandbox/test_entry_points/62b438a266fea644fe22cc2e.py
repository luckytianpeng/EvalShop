"""
62b438a266fea644fe22cc2e
witten/borgmatic
borgmatic/commands/arguments.py
parse_arguments
1109
1180


Given command-line arguments with which this script was invoked, parse the arguments and return
them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.

"""
import sys
import traceback
import pickle

# import ...
from borgmatic.commands.arguments import parse_arguments
from tests.integration.commands.test_arguments import test_parse_arguments_with_multiple_config_paths_parses_as_list

# Test Data

#
exit_code = 0

try:
    result = test_parse_arguments_with_multiple_config_paths_parses_as_list()
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
