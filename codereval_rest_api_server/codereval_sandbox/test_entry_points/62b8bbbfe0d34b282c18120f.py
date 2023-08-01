"""
62b8bbbfe0d34b282c18120f
champax/pysolbase
pysolbase/FileUtility.py
file_to_textbuffer
161
197


Load a file toward a text buffer

"""
import sys
import traceback
import pickle

# import ...
from pysolbase.FileUtility import FileUtility


# Test Data

#
exit_code = 0

try:
    f = FileUtility()
    result = f.file_to_textbuffer('_tmp.txt', encoding='utf-8')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
