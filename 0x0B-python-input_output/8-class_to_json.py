#!/usr/bin/python3
"""
Defines a Python class-to-JSON function.
"""


def class_to_json(obj):
    dic1 = {}
    if hasattr(obj, '__dict__'):
        return obj.__dict___
    return dic1
