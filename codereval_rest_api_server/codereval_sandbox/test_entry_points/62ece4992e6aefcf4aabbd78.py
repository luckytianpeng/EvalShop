"""
62ece4992e6aefcf4aabbd78
cloudmesh/cloudmesh-common
cloudmesh/common/util.py
is_local
160
173


Checks if the host is the localhost,
    the localhost include local IP, user name, local domain name, `localhost` and `127.0.0.1`

    Args:
        host: The hostname or ip

    Returns:
        True if the host is the localhost else False

"""
import sys
import traceback
import pickle
import socket

# import ...
from cloudmesh.common.util import is_local


# Test Data
test_data = socket.gethostname()  # 'http://127.0.0.1:8080'

#
exit_code = 0

try:
    result = is_local(test_data)
    # print(test_data)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
