#!/usr/bin/python3
import json
from models.base_model import BaseModel
"""
A serialization and deserialization module
"""


class FileStorage():
    """
    A serialization and deserialization blueprint.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        First create a key by dot-joining the class-name
        and id of the object.
        Then it updates the __objects dictonary with the
        new object.
        """
        if obj:
            key = '.'.join([obj.__class__.__name__, obj.id])
            self.__objects[key] = obj

    def save(self):
        """
        First convert all obj in the __object to dict, then
        dumps the __object dictionary into a JSON file.
        """
        with open(self.__file_path, 'w') as f:
            dico = {}
            for k,v in self.__objects.items():
                dico[k] = v.to_dict()
            json.dump(dico, f)

    def reload(self):
        """
        Quietly load the JSON back into a python object.
        """
        try:
            with open(self.__file_path, 'r') as f:
                py_obj = json.load(f)
                for k,v in py_obj.items():
                    self.__objects[k] = BaseModel(**v)
            return py_obj
        except Exception as e:
            pass
