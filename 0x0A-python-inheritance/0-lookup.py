#!/usr/bin/python3
"""Returns a list of available attributes and non-callable methods of an object.

    Args:
        obj: An object to inspect.

    Returns:
        A list of attribute names.
"""


class lookup:
    def __init__(self, list):
        """Initializes a new instance of the lookup class"""
        self.list = list

        def __lookup(self):
            return self.list

        list = lookup()
        print(list)
