"""
62e4fb4d85ea9864308902e7
pre-commit/pre-commit
pre_commit/parse_shebang.py
normalize_cmd
65
85


Complement the full path to exe and return it in its original form

"""
import sys
import traceback
import pickle

# import ...
from pre_commit.parse_shebang import normalize_cmd


# Test Data

#
exit_code = 0

try:
    result = normalize_cmd(('git', '--version'))
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
