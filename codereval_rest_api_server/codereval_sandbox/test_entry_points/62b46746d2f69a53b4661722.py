"""
62b46746d2f69a53b4661722
bastikr/boolean
boolean/boolean.py
absorb
1446
1518
"""
import sys
import traceback
import pickle

# import ...
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
    t1 = DualBase(a, b, c, d)
    result = t1.absorb((BooleanAlgebra, ))  # (DualBase, ) (BooleanAlgebra, ) (dict, ) (list, )
    # result = algebra.TRUE.simplify()
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
