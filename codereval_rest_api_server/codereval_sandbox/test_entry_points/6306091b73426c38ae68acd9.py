"""
6306091b73426c38ae68acd9
redhat-openstack/infrared
infrared/core/services/__init__.py
workspace_manager
123
126


Gets the workspace manager via ServiceName.WORKSPACE_MANAGER in cls._get_service()

"""
import sys
import traceback
import pickle

# import ...
from infrared.core.services import CoreServices


# Test Data
#
exit_code = 0

try:
    result = CoreServices.workspace_manager()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
