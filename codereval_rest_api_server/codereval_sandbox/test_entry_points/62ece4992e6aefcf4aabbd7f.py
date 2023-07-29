"""
62ece4992e6aefcf4aabbd7f
openstack/cinder
cinder/image/glance.py
_parse_image_ref
97
109


Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:

"""
import sys
import traceback
import pickle

# import ...
from cinder.image.glance import _parse_image_ref


# Test Data
test_data = 'https://www.myweb.com/imgs/abc.png'

#
exit_code = 0

try:
    result = _parse_image_ref(test_data)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
