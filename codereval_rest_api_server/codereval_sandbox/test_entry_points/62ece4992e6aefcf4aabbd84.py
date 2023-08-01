"""
62ece4992e6aefcf4aabbd84
gopad/gopad-python
gopad/rest.py
is_ipv4
297
304


Test if IPv4 address or not.

   Returns: Boolean, True if target is IPv4 address, else False.

"""
import sys
import traceback
import pickle

# import ...
from gopad.rest import is_ipv4


# Test Data
# Ref:
#   https://en.wikipedia.org/wiki/Internet_Protocol_version_4
#   https://en.wikipedia.org/wiki/IPv6
test_data = [
        '0.0.0.0',
        '255.255.255.255',
        '127.0.0.1',
        '192.168.0.1',
        '333.168.0.1',
        '2001:0db8:0000:0000:0000:8a2e:0370:7334',
        '2001:db8::8a2e:370:7334']

#
exit_code = 0

try:
    result = {i:is_ipv4(i) for i in test_data}
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
