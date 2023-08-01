"""
62b438b566fea644fe22cc70
witten/borgmatic
borgmatic/commands/completion.py
bash_completion
27
67


Produce the borgmatic command by introspecting borgmatic's command-line argument parsers.

"""
import sys
import traceback
import pickle

# import ...
from borgmatic.commands.completion import bash_completion


# Test Data

#
exit_code = 0

try:
    result = bash_completion()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
