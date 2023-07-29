"""
6306091b73426c38ae68acd7
redhat-openstack/infrared
infrared/core/services/__init__.py
ansible_config_manager
133
136


Gets the ansible config manager via ServiceName.ANSIBLE_CONFIG_MANAGER in cls._get_service()

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
    result = CoreServices.ansible_config_manager()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
