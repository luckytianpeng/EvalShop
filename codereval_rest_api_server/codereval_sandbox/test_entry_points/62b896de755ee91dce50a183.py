"""
62b896de755ee91dce50a183
pexip/os-python-dateutil
dateutil/parser/_parser.py
parse
578
665


Parse the date/time string into a :class:`datetime.datetime` object.

:param timestr:
    Any date/time string using the supported formats.

:param default:
    The default datetime object, if this is a datetime object and not
    ``None``, elements specified in ``timestr`` replace elements in the
    default object.

:param ignoretz:
    If set ``True``, time zones in parsed strings are ignored and a
    naive :class:`datetime.datetime` object is returned.

:param tzinfos:
    Additional time zone names / aliases which may be present in the
    string. This argument maps time zone names (and optionally offsets
    from those time zones) to time zones. This parameter can be a
    dictionary with timezone aliases mapping time zone names to time
    zones or a function taking two parameters (``tzname`` and
    ``tzoffset``) and returning a time zone.

    The timezones to which the names are mapped can be an integer
    offset from UTC in seconds or a :class:`tzinfo` object.

    .. doctest::
       :options: +NORMALIZE_WHITESPACE

        >>> from dateutil.parser import parse
        >>> from dateutil.tz import gettz
        >>> tzinfos = {"BRST": -7200, "CST": gettz("America/Chicago")}
        >>> parse("2012-01-19 17:21:00 BRST", tzinfos=tzinfos)
        datetime.datetime(2012, 1, 19, 17, 21, tzinfo=tzoffset(u'BRST', -7200))
        >>> parse("2012-01-19 17:21:00 CST", tzinfos=tzinfos)
        datetime.datetime(2012, 1, 19, 17, 21,
                          tzinfo=tzfile('/usr/share/zoneinfo/America/Chicago'))

    This parameter is ignored if ``ignoretz`` is set.

:param \*\*kwargs:
    Keyword arguments as passed to ``_parse()``.

:return:
    Returns a :class:`datetime.datetime` object or, if the
    ``fuzzy_with_tokens`` option is ``True``, returns a tuple, the
    first element being a :class:`datetime.datetime` object, the second
    a tuple containing the fuzzy tokens.

:raises ParserError:
    Raised for invalid or unknown string format, if the provided
    :class:`tzinfo` is not in a valid format, or if an invalid date
    would be created.

:raises TypeError:
    Raised for non-string or character stream input.

:raises OverflowError:
    Raised if the parsed date exceeds the largest valid C integer on
    your system.

"""
import sys
import traceback
import pickle

# import ...
from dateutil.parser._parser import parser


# Test Data
test_data = '2020-03-20T01:31:12.467113+06:00'

#
exit_code = 0

try:
    p = parser()
    result = p.parse(test_data)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
