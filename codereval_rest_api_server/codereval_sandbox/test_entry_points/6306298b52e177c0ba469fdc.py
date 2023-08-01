"""
6306298b52e177c0ba469fdc
jaywink/federation
federation/entities/diaspora/mappers.py
xml_children_as_dict
55
60


Turn the children of node <xml> into a dict, keyed by tag name.

"""
import sys
import traceback
import pickle
import xml.etree.ElementTree as ET

# import ...
from federation.entities.diaspora.mappers import xml_children_as_dict


# Test Data
test_data = '''\
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''

#
exit_code = 0

try:
    # result = xml_children_as_dict(ET.parse(test_data).getroot())
    result = xml_children_as_dict(ET.ElementTree(ET.fromstring(test_data)).getroot())
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
