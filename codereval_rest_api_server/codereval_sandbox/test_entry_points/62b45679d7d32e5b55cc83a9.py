"""
62b45679d7d32e5b55cc83a9
witten/atticmatic
borgmatic/commands/completion.py
parser_flags
19
24


Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.

"""
import sys
import traceback
import pickle

# import ...
from borgmatic.commands.completion import parser_flags
from argparse import ArgumentParser


# Test Data
DEFAULT_DESTINATION_CONFIG_FILENAME = '/etc/borgmatic/config.yaml'

parser = ArgumentParser(description='Generate a sample borgmatic YAML configuration file.')
parser.add_argument(
    '-s',
    '--source',
    dest='source_filename',
    help='Optional YAML configuration file to merge into the generated configuration, useful for upgrading your configuration',
)
parser.add_argument(
    '-d',
    '--destination',
    dest='destination_filename',
    default=DEFAULT_DESTINATION_CONFIG_FILENAME,
    help=f'Destination YAML configuration file, default: {DEFAULT_DESTINATION_CONFIG_FILENAME}',
)
parser.add_argument(
    '--overwrite',
    default=False,
    action='store_true',
    help='Whether to overwrite any existing destination file, defaults to false',
)

#
exit_code = 0

try:
    result = parser_flags(parser)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
