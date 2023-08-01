"""
62b43425903eeb48555d3ea1
cpburnz/python-sql-parameters
sqlparams/__init__.py
_create_in_regex
383
414


Create the in-style parameter regular expression.

Returns the in-style parameter regular expression (:class:`re.Pattern`).

"""
import sys
import traceback
import pickle

# import ...
import sqlparams


# Test Data

#
exit_code = 0

try:
    query = sqlparams.SQLParams('named', 'qmark')
    # print(query)
    print(pickle.dumps(query))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
