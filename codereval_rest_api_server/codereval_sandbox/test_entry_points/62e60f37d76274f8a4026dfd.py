"""
62e60f37d76274f8a4026dfd
neo4j/neo4j-python-driver
src/neo4j/_codec/hydration/v1/temporal.py
dehydrate_time
96
114
"""
import sys
import traceback
import pickle
from datetime import time

from src.neo4j._codec.hydration.v1.temporal import dehydrate_time

# Test Data
test_data = time(13, 24, 56)

#
exit_code = 0

try:
    result = dehydrate_time(test_data)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
