"""
62e60f33d76274f8a4026de9
neo4j/neo4j-python-driver
src/neo4j/_codec/hydration/v1/spatial.py
dehydrate_point
44
57
"""
import sys
import traceback
import pickle

from src.neo4j._codec.hydration.v1.spatial import dehydrate_point, hydrate_point

# Test Data

# Ref:
# - https://www.cockroachlabs.com/docs/stable/srid-4326.html#:~:text=The%20SRID%20is%20used%20to,Global%20Positioning%20System%20(GPS).
test_data = hydrate_point(4326, 1.23, 4.56)

#
exit_code = 0

try:
    result = dehydrate_point(test_data)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
