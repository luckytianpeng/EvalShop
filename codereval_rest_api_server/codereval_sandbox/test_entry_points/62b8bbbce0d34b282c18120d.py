"""
62b8bbbce0d34b282c18120d
champax/pysolbase
pysolbase/FileUtility.py
is_file_exist
60
79


Check whether file_name is an existing file.

"""
import sys
import traceback
import pickle

# import ...
from pysolbase.FileUtility import FileUtility


# Test Data
# test_data = 

#
exit_code = 0

try:
    f = FileUtility()
    result = f.is_file_exist(__file__)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
