"""
62ece4992e6aefcf4aabbd85
mwatts15/rdflib
rdflib/util.py
find_roots
384
407


 Find the roots in some sort of transitive hierarchy.

    find_roots(graph, rdflib.RDFS.subClassOf)
    will return a set of all roots of the sub-class hierarchy

    Assumes triple of the form (child, prop, parent), i.e. the direction of
    RDFS.subClassOf or SKOS.broader

    Args:
        graph: Graph Class Object
        prop: URIRef Class Object
        roots: Optional list with set type
    Return:
        roots: a set with nodes

"""
import sys
import traceback
import pickle

# import ...
from rdflib.util import find_roots
import rdflib
from rdflib.graph import Graph
from rdflib.term import URIRef
# from test.test_util import test_find_roots


# Test Data

#
exit_code = 0

try:
    g = Graph('Memory', URIRef("https://rdflib.github.io"))
    result = find_roots(g, rdflib.RDFS.subClassOf)
    # print(result)
    # result = None  # test_find_roots()
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
