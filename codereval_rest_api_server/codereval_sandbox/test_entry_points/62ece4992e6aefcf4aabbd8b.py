"""
62ece4992e6aefcf4aabbd8b
awsteiner/o2sclpy
o2sclpy/utils.py
force_string
109
116
"""
import sys
import traceback
import pickle

# import ...
from o2sclpy.utils import force_string

# Test Data
test_data ='''\
name:
    Pythagoras:
time:
    575–500 BCE
works:
    - Pythagorean theorem (gou-gu theorem in ancient Chinese literature)
'''
#
exit_code = 0

try:
    result = force_string(test_data)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
