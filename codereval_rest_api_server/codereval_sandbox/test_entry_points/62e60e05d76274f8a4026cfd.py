"""
62e60e05d76274f8a4026cfd
neo4j/neo4j-python-driver
src/neo4j/_data.py
index
161
178
"""
import sys
import traceback
import pickle
import time

# from src.neo4j.work.query import unit_of_work
from src.neo4j._data import Record


# Test Data
test_data = Record({'x': 1, 'y': 2, 'z': 3, 't': 4})

#
exit_code = 0

try:
    result = test_data.index('t')
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
