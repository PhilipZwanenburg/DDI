#!/usr/bin/env python3
#
# This file is part of DDI.
#
# DDI is free software: you can redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either version 3 of the License, or
# any later version. DDI is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with DDI. If not, see
# <http://www.gnu.org/licenses/>.
## \file

import tensorflow as tf
import numpy as np

def myfunction(arg1, arg2, kwarg='whatever.'):
    """
    Does nothing more than demonstrate syntax.

    This is an example of how a Pythonic human-readable docstring can
    get parsed by doxypypy and marked up with Doxygen commands as a
    regular input filter to Doxygen.

    \todo Delete this function once other examples are present.

    Args:
        arg1:   A positional argument.
        arg2:   Another positional argument.

    Kwargs:
        kwarg:  A keyword argument.

    Returns:
        A string holding the result.

    Raises:
        ZeroDivisionError: if `arg2` = 0
        AssertionError
        ValueError


    Examples:
        >>> myfunction(2, 3)
        '5 - 0, whatever.'
        >>> myfunction(5, 0, 'oops.')
        Traceback (most recent call last):
            ...
        ZeroDivisionError: integer division or modulo by zero
        >>> myfunction(4, 1, 'got it.')
        '5 - 4, got it.'
        >>> myfunction(23.5, 23, 'oh well.')
        Traceback (most recent call last):
            ...
        AssertionError
        >>> myfunction(5, 50, 'too big.')
        Traceback (most recent call last):
            ...
        ValueError
    """
    assert isinstance(arg1, int)
    if arg2 > 23:
        raise ValueError
    return '{0} - {1}, {2}'.format(arg1 + arg2, arg1 / arg2, kwarg)

if __name__ == "__main__":
	"""
	Note that comments in __main__ docstring do not appear in doxygen documentation.
	"""

	print("In main.")
