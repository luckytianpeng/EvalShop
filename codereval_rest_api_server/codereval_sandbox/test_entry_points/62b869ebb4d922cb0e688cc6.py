"""
62b869ebb4d922cb0e688cc6
rak-n-rok/Krake
krake/krake/controller/kubernetes/hooks.py
update_last_applied_manifest_list_from_resp
301
351


Together with :func:``update_last_applied_manifest_dict_from_resp``, this
function is called recursively to update a partial ``last_applied_manifest``
from a partial Kubernetes response

Args:
    last_applied_manifest (list): partial ``last_applied_manifest`` being
        updated
    observer_schema (list): partial ``observer_schema``
    response (list): partial response from the Kubernetes API.

This function go through all observed fields, and initialized their value in
last_applied_manifest if they are not yet present

"""
import sys
import traceback
import pickle

# import ...


# Test Data
# test_data = 

#
exit_code = 0

try:
    result = test_function(test_data)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
