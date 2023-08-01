"""
62e60723d76274f8a4026b76
neo4j/neo4j-python-driver
src/neo4j/time/__init__.py
from_ticks
1506
1528


Create a time from ticks (nanoseconds since midnight).

:param ticks: nanoseconds since midnight
:type ticks: int
:param tz: optional timezone
:type tz: datetime.tzinfo

:rtype: Time

:raises ValueError: if ticks is out of bounds
    (0 <= ticks < 86400000000000)

"""
import sys
import traceback
import pickle

# import ...
from src.neo4j.time import Time


# Test Data
# test_data = 

#
exit_code = 0

try:
    result = Time.from_ticks(int(86400000000000/2))
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
