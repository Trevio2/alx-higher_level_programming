#!/usr/bin/python3
"""Returns True if the object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """This function returns True if the object is an instance of a class"""
    return issubclass(obj, a_class)
