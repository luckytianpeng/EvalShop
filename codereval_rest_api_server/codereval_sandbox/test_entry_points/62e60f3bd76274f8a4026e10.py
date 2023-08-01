"""
62e60f3bd76274f8a4026e10
neo4j/neo4j-python-driver
src/neo4j/_codec/hydration/v1/temporal.py
dehydrate_timedelta
256
267
"""
import sys
import traceback
import pickle
from datetime import timedelta

from src.neo4j._codec.hydration.v1.temporal import dehydrate_timedelta


# Test Data
test_data = timedelta(
        days=50,
        seconds=27,
        microseconds=10,
        milliseconds=29000,
        minutes=5,
        hours=8,
        weeks=2)

#
exit_code = 0

try:
    result = dehydrate_timedelta(test_data)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
