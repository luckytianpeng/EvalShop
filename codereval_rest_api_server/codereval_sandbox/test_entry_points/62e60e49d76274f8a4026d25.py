"""
62e60e49d76274f8a4026d25
neo4j/neo4j-python-driver
src/neo4j/_work/query.py
unit_of_work
56
110
"""
import sys
import traceback
import pickle
import time

# from src.neo4j.work.query import unit_of_work

# Test Data

from neo4j import unit_of_work

@unit_of_work(timeout=5, metadata={"applicationId": "123"})
def create_person(tx, name):
    return tx.run(
        "CREATE (a:Person {name: $name}) RETURN id(a)", name=name
    ).single().value()

#
exit_code = 0

try:
    result = {
            'timeout': create_person.timeout,
            'metadata': create_person.metadata}
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
