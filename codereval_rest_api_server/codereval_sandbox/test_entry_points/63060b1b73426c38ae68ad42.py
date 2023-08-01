"""
63060b1b73426c38ae68ad42
redhat-openstack/infrared
infrared/core/services/ansible_config.py
inject_config
94
97


If the ANSIBLE_CONFIG property does not exist in os.environ, set it to self.ansible_config_path.

"""
import sys
import traceback
import pickle

# import ...
from infrared.core.services.ansible_config import AnsibleConfigManager


# Test Data

#
exit_code = 0

try:
    a = AnsibleConfigManager(infrared_home='')
    result = a.inject_config()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
