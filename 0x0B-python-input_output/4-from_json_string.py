#!/usr/bin/python3
"""Convert to an object from a json format"""
import json


def from_json_string(my_str):
    """returns the an object representation of a JSON string"""

    return json.loads(my_str)
