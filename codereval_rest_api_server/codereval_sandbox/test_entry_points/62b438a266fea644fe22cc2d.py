"""
62b438a266fea644fe22cc2d
witten/borgmatic
borgmatic/commands/arguments.py
parse_subparser_arguments
52
148


Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
instance, give each requested action's subparser a shot at parsing all arguments. This allows
common arguments like "--repository" to be shared across multiple subparsers.

Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
arguments, a list of remaining arguments not claimed by any subparser).

"""
import sys
import traceback
import pickle

# import ...
from borgmatic.commands.arguments import parse_subparser_arguments
from tests.unit.commands.test_arguments import test_parse_subparser_arguments_consumes_subparser_arguments_before_subparser_name


# Test Data

#
exit_code = 0

try:
    result = test_parse_subparser_arguments_consumes_subparser_arguments_before_subparser_name()
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
