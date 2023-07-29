"""
6306091c73426c38ae68acdc
redhat-openstack/infrared
infrared/core/utils/validators.py
validate_from_content
96
136


validates that spec (YAML) content has all required fields

:param spec_content: content of spec file
:raise IRValidatorException: when mandatory data
is missing in spec file
:return: Dictionary with data loaded from a spec (YAML) file

"""
import sys
import traceback
import pickle

# import ...
from infrared.core.utils.validators import SpecValidator

# Test Data
# tests/example/plugins/add_remove_all_plugins/install_plugin1/plugin.spec
test_data = '''\
plugin_type: install
subparsers:
    install_plugin1:
        description: install_plugin1 desc
        include_groups: []
'''

#
exit_code = 0

try:
    result = SpecValidator.validate_from_content(test_data)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
