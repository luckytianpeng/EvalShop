"""
62b46740d2f69a53b466171a
bastikr/boolean
boolean/boolean.py
pretty
1024
1033
"""
import sys
import traceback
import pickle

# import ...
from boolean.boolean import Symbol
from boolean.boolean import Symbol, BooleanAlgebra, DualBase

# Test Data
algebra = BooleanAlgebra()
a = algebra.Symbol("a")
b = algebra.Symbol("b")
c = algebra.Symbol("c")
d = algebra.Symbol("d")

test_expression = (
    ~a & ~b & ~c & ~d
    | ~a & ~b & ~c & d
    | ~a & b & ~c & ~d
    | ~a & b & c & d
    | ~a & b & ~c & d
    | ~a & b & c & ~d
    | a & ~b & ~c & d
    | ~a & b & c & d
    | a & ~b & c & d
    | a & b & c & d
)
#
exit_code = 0

try:
    s = Symbol(test_expression)
    result = s.pretty(indent=4, debug=True)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
