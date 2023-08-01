"""
63060b1a73426c38ae68ad3e
redhat-openstack/infrared
tests/test_plugins.py
get_plugin_spec_flatten_dict
139
165


Use YAML to read various information in plugin_dir and return the information in dictionary form.

"""
import sys
import traceback
import pickle

# import ...
from tests.test_plugins import get_plugin_spec_flatten_dict


# Test Data
test_data = '''tests/example/plugins/plugin_with_src_path/infrared_plugin/'''

#
exit_code = 0

try:
    result = get_plugin_spec_flatten_dict(test_data)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
