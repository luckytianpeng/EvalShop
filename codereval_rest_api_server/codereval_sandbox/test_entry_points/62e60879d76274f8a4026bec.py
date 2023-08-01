"""
62e60879d76274f8a4026bec
neo4j/neo4j-python-driver
src/neo4j/_async/io/_bolt3.py
begin
293
339
"""
import sys
import traceback
import pickle

import pytest

from tests.unit.sync.io.conftest import FakeSocket

import neo4j
from neo4j._conf import PoolConfig
from neo4j._sync.io._bolt3 import Bolt3
from neo4j.exceptions import ConfigurationError

from tests._async_compat import mark_sync_test

# Test Data

@mark_sync_test
def test_simple_begin(fake_socket):
    address = neo4j.Address(("127.0.0.1", 7687))
    socket = fake_socket(address, Bolt3.UNPACKER_CLS)
    connection = Bolt3(address, socket, PoolConfig.max_connection_lifetime)

    with pytest.raises(ConfigurationError):
        connection.begin(db='something')

    connection.begin()
    connection.send_all()
    tag, fields = socket.pop_message()
    assert tag == b"\x11"
    assert len(fields) == 1

#
exit_code = 0

try:
    result = test_simple_begin(fake_socket=FakeSocket)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
