"""
62ece4982e6aefcf4aabbd76
bazaar-projects/docopt-ng
docopt/__init__.py
match
211
214
"""
import sys
import traceback
import pickle

# import ...
from docopt import docopt


# Test Data
doc = """Usage: prog [-vqr] [FILE]
            prog INPUT OUTPUT
            prog --help

Options:
    -v  print status messages
    -q  report only file names
    -r  show all occurrences of the same error
    --help

"""
#
exit_code = 0

try:
    a = dict(docopt(doc, "-v Doxyfile"))
    assert a == {
        "-v": True,
        "-q": False,
        "-r": False,
        "--help": False,
        "FILE": "Doxyfile",
        "INPUT": None,
        "OUTPUT": None,
    }
    # print(a)
    print(pickle.dumps(dict(a)))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
