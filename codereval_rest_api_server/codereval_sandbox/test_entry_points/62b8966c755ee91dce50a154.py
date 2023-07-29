"""
62b8966c755ee91dce50a154
pexip/os-python-dateutil
dateutil/parser/isoparser.py
isoparse
59
146


Parse an ISO-8601 datetime string into a :class:`datetime.datetime`.

An ISO-8601 datetime string consists of a date portion, followed
optionally by a time portion - the date and time portions are separated
by a single character separator, which is ``T`` in the official
standard. Incomplete date formats (such as ``YYYY-MM``) may *not* be
combined with a time portion.

Supported date formats are:

Common:

- ``YYYY``
- ``YYYY-MM`` or ``YYYYMM``
- ``YYYY-MM-DD`` or ``YYYYMMDD``

Uncommon:

- ``YYYY-Www`` or ``YYYYWww`` - ISO week (day defaults to 0)
- ``YYYY-Www-D`` or ``YYYYWwwD`` - ISO week and day

The ISO week and day numbering follows the same logic as
:func:`datetime.date.isocalendar`.

Supported time formats are:

- ``hh``
- ``hh:mm`` or ``hhmm``
- ``hh:mm:ss`` or ``hhmmss``
- ``hh:mm:ss.ssssss`` (Up to 6 sub-second digits)

Midnight is a special case for `hh`, as the standard supports both
00:00 and 24:00 as a representation. The decimal separator can be
either a dot or a comma.


.. caution::

    Support for fractional components other than seconds is part of the
    ISO-8601 standard, but is not currently implemented in this parser.

Supported time zone offset formats are:

- `Z` (UTC)
- `±HH:MM`
- `±HHMM`
- `±HH`

Offsets will be represented as :class:`dateutil.tz.tzoffset` objects,
with the exception of UTC, which will be represented as
:class:`dateutil.tz.tzutc`. Time zone offsets equivalent to UTC (such
as `+00:00`) will also be represented as :class:`dateutil.tz.tzutc`.

:param dt_str:
    A string or stream containing only an ISO-8601 datetime string

:return:
    Returns a :class:`datetime.datetime` representing the string.
    Unspecified components default to their lowest value.

.. warning::

    As of version 2.7.0, the strictness of the parser should not be
    considered a stable part of the contract. Any valid ISO-8601 string
    that parses correctly with the default settings will continue to
    parse correctly in future versions, but invalid strings that
    currently fail (e.g. ``2017-01-01T00:00+00:00:00``) are not
    guaranteed to continue failing in future versions if they encode
    a valid date.

.. versionadded:: 2.7.0

"""
import sys
import traceback
import pickle

# import ...
from dateutil.parser.isoparser import isoparser


# Test Data
test_data = '2020-03-20T01:31:12.467113+06:00'

#
exit_code = 0

try:
    i = isoparser()
    result = i.isoparse(test_data)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
