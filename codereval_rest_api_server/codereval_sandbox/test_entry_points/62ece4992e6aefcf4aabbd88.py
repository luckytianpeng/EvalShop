"""
62ece4992e6aefcf4aabbd88
sunpy/radiospectra
radiospectra/spectrogram.py
make_array
929
940


Returns a 0-filled array of the given shape and type.

        Args:
                shape : tuple
                    shape of the array to create
                dtype : `numpy.dtype`
                    data-type of the array to create
        Return: array

"""
import sys
import traceback
import pickle
from datetime import datetime


# import ...
import numpy as np
from radiospectra.spectrogram import LinearTimeSpectrogram


# Test Data

#
exit_code = 0

try:
    image = np.zeros((200, 3600))
    li = LinearTimeSpectrogram(
        image,
        np.linspace(0, image.shape[1] - 1, image.shape[1]),
        np.linspace(0, image.shape[0] - 1, image.shape[0]),
        datetime(2010, 10, 10),
        datetime(2010, 10, 10, 1),
        0,
        1,
    )
    result = li.make_array([3, 3], float)
    # print(result)
    print(pickle.dumps(result))
except:
    print(traceback.print_exc(), file=sys.stderr)
    exit_code = 1

exit(exit_code)
