"""
62e60f43d76274f8a4026e28
neo4j/neo4j-python-driver
src/neo4j/_codec/hydration/v1/temporal.py
hydrate_time
77
93
"""
import sys
import traceback
import pickle

from src.neo4j._codec.hydration.v1.temporal import hydrate_time

# Test Data
test_data = 3723000000004

#
exit_code = 0

try:
    result = hydrate_time(test_data)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
