"""
62ece4992e6aefcf4aabbd8a
witten/borgmatic
borgmatic/commands/borgmatic.py
load_configurations
496
541


Given a sequence of configuration filenames, load and validate each configuration file. If the configuration file
cannot be read due to insufficient permissions or error parsing configuration file, the error log will
be recorded. Otherwise, return the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
and sequence of logging.LogRecord instances containing any parse errors.

"""
import sys
import traceback
import pickle

# import ...
from borgmatic.commands.borgmatic import load_configurations


# Test Data

#
exit_code = 0

try:
    result = load_configurations('./borgmatic/config/schema.yaml')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
