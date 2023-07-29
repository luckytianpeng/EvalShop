"""
62ece4992e6aefcf4aabbd86
ansible-security/ansible_collections.ibm.qradar
tests/unit/mock/yaml_helper.py
_dump_string
28
33
"""
import sys
import traceback
import pickle
import yaml

from ansible.parsing.yaml.dumper import AnsibleDumper
from tests.unit.mock.yaml_helper import YamlTestUtils


# Test Data
test_data ='''\
name:
    Thales of Miletus
time:
    624–546 BCE
works:
    - Thales's theorem
'''


# print(yaml.safe_load(test_data))

#
exit_code = 0

try:
    y = YamlTestUtils()
    result = y._dump_string(yaml.safe_load(test_data), AnsibleDumper)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
