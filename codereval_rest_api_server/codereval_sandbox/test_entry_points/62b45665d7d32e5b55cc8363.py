"""
62b45665d7d32e5b55cc8363
witten/atticmatic
borgmatic/commands/arguments.py
make_parsers
165
1091


Build a parser and its subparsers and return them as a tuple.

"""
import sys
import traceback
import pickle

# import ...
from borgmatic.commands.arguments import make_parsers
# from tests.unit.commands.test_arguments import test_parse_subparser_arguments_parses_borg_options_and_skips_other_subparsers


# Test Data

#
exit_code = 0

try:
    result = make_parsers()  # test_parse_subparser_arguments_parses_borg_options_and_skips_other_subparsers()
    print(result)
    # print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
