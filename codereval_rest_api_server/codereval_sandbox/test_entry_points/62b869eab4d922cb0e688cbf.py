"""
62b869eab4d922cb0e688cbf
rak-n-rok/Krake
krake/krake/controller/kubernetes/hooks.py
generate_default_observer_schema
1172
1197


Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.

"""
import sys
import traceback
import pickle

# import ...
from krake.krake.data.kubernetes import Application
from krake.krake.controller.kubernetes.hooks import generate_default_observer_schema


# Test Data

#
exit_code = 0

try:
    app = Application()
    result = generate_default_observer_schema(app)
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
