"""
62ece4982e6aefcf4aabbd65
witten/borgmatic
borgmatic/commands/completion.py
parser_flags
19
24


Given an argparse.ArgumentParser instance, return its argument flags in a space-separated string.
    Args:
        script: argparse.ArgumentParser instance

    Returns:
        argument flags in a space-separated string

"""
import sys
import traceback
import pickle

# import ...
from borgmatic.commands import arguments
from borgmatic.commands.completion import parser_flags


# Test Data
top_level_parser, subparsers = arguments.make_parsers()

#
exit_code = 0

try:
    global_flags = parser_flags(top_level_parser)
    # print(global_flags)
    print(pickle.dumps(global_flags))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
