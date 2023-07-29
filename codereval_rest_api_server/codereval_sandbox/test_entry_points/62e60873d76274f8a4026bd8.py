"""
62e60873d76274f8a4026bd8
neo4j/neo4j-python-driver
src/neo4j/_async/io/_bolt.py
protocol_handlers
238
291


Return a dictionary of available Bolt protocol handlers,
keyed by version tuple. If an explicit protocol version is
provided, the dictionary will contain either zero or one items,
depending on whether that version is supported. If no protocol
version is provided, all available versions will be returned.

:param protocol_version: tuple identifying a specific protocol
    version (e.g. (3, 5)) or None
:return: dictionary of version tuple to handler class for all
    relevant and supported protocol versions
:raise TypeError: if protocol version is not passed in a tuple

"""
import sys
import traceback
import pickle

# import ...
from src.neo4j._async.io._bolt import AsyncBolt

# Test Data
# test_data = 

#
exit_code = 0

try:
    result = AsyncBolt.protocol_handlers()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
