"""
62b4567ed7d32e5b55cc83d9
witten/atticmatic
borgmatic/config/load.py
deep_merge_nodes
165
286


Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.

"""
import sys
import traceback
import pickle

# import ...
from borgmatic.config.load import deep_merge_nodes
from tests.integration.config.test_load import test_deep_merge_nodes_replaces_colliding_scalar_values


# Test Data

#
exit_code = 0

try:
    result = test_deep_merge_nodes_replaces_colliding_scalar_values()
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
