"""
6306091a73426c38ae68acc8
redhat-openstack/infrared
tests/test_complex_types.py
list_of_file_names
229
233


Create and return a new IniType complex type via cli.ListOfFileNames()

"""
import sys
import traceback
import pickle

# import ...
from tests.test_complex_types import test_list_of_file_names_values_auto_propagation


# Test Data

#
exit_code = 0

try:
    result = test_list_of_file_names_values_auto_propagation()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
