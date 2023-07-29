"""
62b438a266fea644fe22cc2c
witten/borgmatic
borgmatic/commands/arguments.py
make_parsers
165
1091


Build a top-level parser and its subparsers and return them as a tuple.

"""
import sys
import traceback
import pickle

# import ...
from borgmatic.commands.arguments import make_parsers


# Test Data

#
exit_code = 0

try:
    result = make_parsers()
    print(result)
    # print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
