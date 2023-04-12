#!/usr/bin/python3
"""This module contains a class that inherits"""


class Mylist(list):
    """class derived from previous list"""
    def print_sorted(self):
        print(sorted(self))
