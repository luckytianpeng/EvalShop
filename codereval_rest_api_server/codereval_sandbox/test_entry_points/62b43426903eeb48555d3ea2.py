"""
62b43426903eeb48555d3ea2
cpburnz/python-sql-parameters
sqlparams/__init__.py
_create_converter
293
381


Create the parameter style converter.

Returns the parameter style converter (:class:`._converting._Converter`).

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
