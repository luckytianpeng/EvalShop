"""
62ece4982e6aefcf4aabbd73
cloudmesh/cloudmesh-common
cloudmesh/common/shlex.py
split
7
53


Split the input str under given platform, return the splitting result
    If platform equals 'this', auto-detect current platform.
    If platform equals 1, use POSIX style.
    If platform equals 0, use Windows/CMD style.
    Args:
        s: input str
        platform: 'this' = auto from current platform; 1 = POSIX; 0 = Windows/CMD
    Returns:
        a list of splitting str

"""
import sys
import traceback
import pickle

# import ...
from cloudmesh.common.shlex import split

# Test Data
test_data = 'ffmpeg -i video.mp4 video.avi'

#
exit_code = 0

try:
    result = split(test_data)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
