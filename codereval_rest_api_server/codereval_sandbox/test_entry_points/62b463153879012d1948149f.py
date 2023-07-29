"""
62b463153879012d1948149f
scieloorg/packtools
packtools/sps/models/packages.py
_eval_file
242
293


Identify the type of the given file. Return None if the file do not match the given prefix or the type of the file is xml. Return dict with the key of component_id, file_path if the type of the file is "pdf", return dict with the key of component_id, file_path, ftype, file_path if the type of the file is not "pdf".

"""
import sys
import traceback
import pickle

# import ...
from packtools.sps.models.packages import _eval_file


# Test Data

#
exit_code = 0

try:
    result = _eval_file('0034-8910-rsp-48-2-0357', '0034-8910-rsp-48-2-0357.json')
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
