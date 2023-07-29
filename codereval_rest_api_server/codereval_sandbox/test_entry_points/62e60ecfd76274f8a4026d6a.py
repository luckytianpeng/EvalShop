"""
62e60ecfd76274f8a4026d6a
neo4j/neo4j-python-driver
src/neo4j/_sync/io/_bolt.py
protocol_handlers
239
291
"""
import sys
import traceback
import pickle

from src.neo4j._sync.io._bolt import Bolt


# Test Data

#
exit_code = 0

try:
    protocol_handlers = Bolt.protocol_handlers(protocol_version=(4, 3))
    result = protocol_handlers
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
