"""
62b8bbbfe0d34b282c181210
champax/pysolbase
pysolbase/FileUtility.py
append_text_to_file
232
271


Writes the data in the text buffer to a file

"""
import sys
import traceback
import pickle

# import ...
from pysolbase.FileUtility import FileUtility


# Test Data
test_data = '''\
Euclid:
Greek (ca. 300 BCE)
Elements
'''

#
exit_code = 0

try:
    f = FileUtility()
    result = f.append_text_to_file('_tmp.txt', test_data, encoding='utf-8', overwrite=True)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
