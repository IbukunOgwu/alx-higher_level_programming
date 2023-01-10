#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serilalization of an object """
    return obj.__dict___
