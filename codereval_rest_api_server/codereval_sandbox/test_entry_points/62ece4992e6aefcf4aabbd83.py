"""
62ece4992e6aefcf4aabbd83
burgerbecky/makeprojects
makeprojects/build_objects.py
run_command
173
197

A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)

"""
import sys
import traceback
import pickle

# import ...
from makeprojects.build_objects import BuildObject

# Test Data
# test_data = 

#
exit_code = 0

try:
    obj = BuildObject(file_name='./')
    result = obj.run_command(f'ls', verbose=True)
    print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
