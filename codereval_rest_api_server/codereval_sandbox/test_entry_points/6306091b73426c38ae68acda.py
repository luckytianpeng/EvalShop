"""
6306091b73426c38ae68acda
redhat-openstack/infrared
infrared/core/services/__init__.py
plugins_manager
128
131


Gets the plugin manager via ServiceName.PLUGINS_MANAGER in cls._get_service()

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
    result = CoreServices.plugins_manager()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
