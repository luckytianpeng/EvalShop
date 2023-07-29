"""
62e6087bd76274f8a4026bfa
neo4j/neo4j-python-driver
src/neo4j/_codec/packstream/v1/__init__.py
pop_u16
508
517
"""
import sys
import traceback
import pickle

from src.neo4j._codec.packstream.v1 import UnpackableBuffer


# Test Data

#
exit_code = 0

try:
    ub = UnpackableBuffer(b'12345')
    result = ub.pop_u16()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
