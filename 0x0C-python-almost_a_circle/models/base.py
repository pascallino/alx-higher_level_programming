#!/usr/bin/python3
""" BASE MODEL CLASS / SUPER CLASS"""
import json


class Base:
    """ base class from which other classes will be derived"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor __init__ """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ base to json string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
    @classmethod
    def create(cls, **dictionary):
        """ self initialization of an object and setting attributes 
        within the class using the update method
        """
        dummy_instance = cls()
        dummy_instance.update(**dictionary)
        return dummy_instance
