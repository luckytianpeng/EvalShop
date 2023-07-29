"""
62b45665d7d32e5b55cc8364
witten/atticmatic
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
from flexmock import flexmock
from borgmatic.commands import arguments as module
from borgmatic.commands.arguments import parse_subparser_arguments


# Test Data
action_namespace = flexmock(foo=True)
subparsers = {
    'action': flexmock(parse_known_args=lambda arguments: (action_namespace, ['action'])),
    'other': flexmock(),
}

#
exit_code = 0

try:
    arguments, remaining_arguments = module.parse_subparser_arguments(
                ('--foo', 'true', 'action'), subparsers
            )
    # print(arguments)
    # print(remaining_arguments)
    assert arguments == {'action': action_namespace}
    assert remaining_arguments == []
    result = None
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
