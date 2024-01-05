#!/usr/bin/python3
"""Defines a class LockedClass"""


class LockedClass:
    """
        LockedClass does nothing
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances of Locked Class."""

        self.first_name = "first_name"
