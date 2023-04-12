#!/usr/bin/python3
"""Returns a list of available attributes and methods.

    Args:
        obj: An object to inspect.

    Returns:
        A list of attribute names.
"""


def lookup(obj):
    """Returns the list of attributes and methods"""
    return dir(obj)
