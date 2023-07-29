"""
62e60e3bd76274f8a4026d1a
neo4j/neo4j-python-driver
src/neo4j/api.py
from_raw_values
283
305


Create a Bookmarks object from a list of raw bookmark string values.

"""
import sys
import traceback
import pickle

# import ...
from src.neo4j.api import Bookmarks


# Test Data
# test_data = 

#
exit_code = 0

try:
    result = Bookmarks.from_raw_values(("bm1", "bm2"))
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
