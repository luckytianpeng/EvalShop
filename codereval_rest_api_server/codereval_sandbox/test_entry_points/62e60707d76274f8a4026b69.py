"""
62e60707d76274f8a4026b69
neo4j/neo4j-python-driver
src/neo4j/_spatial/__init__.py
point_type
85
118


Dynamically Generating Point Class

"""
import sys
import traceback
import pickle

# import ...
# from src.neo4j._spatial import point_type
from tests.unit.common.spatial.test_point import TestPoint


# Test Data

#
exit_code = 0

try:
    t = TestPoint()
    result = t.test_immutable_coordinates()
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
