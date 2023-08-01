"""
62e60723d76274f8a4026b75
neo4j/neo4j-python-driver
src/neo4j/time/_arithmetic.py
round_half_to_even
106
135


Round a floating-point number

"""
import sys
import traceback
import pickle

# import ...
from src.neo4j.time._arithmetic import round_half_to_even


# Test Data
test_data = [3, 3.2, 3.5, 3.7, 4, 4.2, 4.5, 4.7]

#
exit_code = 0

try:
    result = [round_half_to_even(i) for i in test_data]
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
