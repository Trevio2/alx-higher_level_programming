#!/usr/bin/python3
"""Returns a list of available attributes and non-callable methods of an object.

    Args:
        obj: An object to inspect.

    Returns:
        A list of attribute names.
"""


def lookup(object):
    """Returns the list of available attributes and methods of an object"""
    return dir(object)
