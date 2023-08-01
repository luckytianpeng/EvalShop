"""
62e60b10d76274f8a4026ccd
neo4j/neo4j-python-driver
src/neo4j/_data.py
data
245
259
"""
import sys
import traceback
import pickle

# from src.neo4j.work.query import unit_of_work
from src.neo4j._data import Record


# Test Data
test_data = Record({'x': 1, 'y': 2, 'z': 3, 't': 4})

#
exit_code = 0

try:
    result = test_data.data('t', 'z', 'y', 'x')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
