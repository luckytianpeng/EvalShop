"""
62e6087ad76274f8a4026bf2
neo4j/neo4j-python-driver
src/neo4j/_async/io/_bolt3.py
discard
277
283
"""
import sys
import traceback
import pickle

from tests.unit.sync.io.conftest import FakeSocket
from tests.unit.sync.io.test_class_bolt3 import test_simple_discard


# Test Data

#
exit_code = 0

try:
    result = test_simple_discard(fake_socket=FakeSocket)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
