"""
62ece4992e6aefcf4aabbd7b
witten/borgmatic
borgmatic/config/generate.py
write_configuration
112
131


Given a rendered config YAML, write it out to target file.
    But if the file already exists and overwrite is False,
    abort before writing anything.
    If the file does not exist, create it.
    Write to the file otherwise.

    Returns: None

"""
import sys
import traceback
import pickle

# import ...
from borgmatic.config.generate import write_configuration

# Test Data
test_data = '''\
---
 doe: "a deer, a female deer"
 ray: "a drop of golden sun"
 pi: 3.14159
 xmas: true
 french-hens: 3
 calling-birds:
   - huey
   - dewey
   - louie
   - fred
 xmas-fifth-day:
   calling-birds: four
   french-hens: 3
   golden-rings: 5
   partridges:
     count: 1
     location: "a pear tree"
   turtle-doves: two
'''

#
exit_code = 0

try:
    result = write_configuration(f'{__file__}.yaml', test_data, overwrite=True)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
