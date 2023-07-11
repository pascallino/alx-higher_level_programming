#!/usr/bin/python3
import json
""" json function """


def from_json_string(my_str):
    """ function to deserialize to string """
    return json.loads(my_str)
