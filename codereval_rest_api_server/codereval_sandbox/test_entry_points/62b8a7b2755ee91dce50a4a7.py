"""
62b8a7b2755ee91dce50a4a7
pexip/os-python-dateutil
dateutil/utils.py
default_tzinfo
29
61


Sets the ``tzinfo`` parameter on naive datetimes only

This is useful for example when you are provided a datetime that may have
either an implicit or explicit time zone, such as when parsing a time zone
string.

.. doctest::

    >>> from dateutil.tz import tzoffset
    >>> from dateutil.parser import parse
    >>> from dateutil.utils import default_tzinfo
    >>> dflt_tz = tzoffset("EST", -18000)
    >>> print(default_tzinfo(parse('2014-01-01 12:30 UTC'), dflt_tz))
    2014-01-01 12:30:00+00:00
    >>> print(default_tzinfo(parse('2014-01-01 12:30'), dflt_tz))
    2014-01-01 12:30:00-05:00

:param dt:
    The datetime on which to replace the time zone

:param tzinfo:
    The :py:class:`datetime.tzinfo` subclass instance to assign to
    ``dt`` if (and only if) it is naive.

:return:
    Returns an aware :py:class:`datetime.datetime`.

"""
import sys
import traceback
import pickle

# import ...
from dateutil.tz import tzoffset
from dateutil.parser import parse
from dateutil.utils import default_tzinfo


# Test Data
dflt_tz = tzoffset("EST", -18000)

#
exit_code = 0

try:
    result = default_tzinfo(parse('2014-01-01 12:30 UTC'), dflt_tz)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
