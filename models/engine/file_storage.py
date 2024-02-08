#!/usr/bin/python3
import json
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
            self.__objects.update({key: obj.__dict__})

    def save(self):
        """
        Dumps the __object dictionary into a JSON file.
        """
        with open(self.__file_path, 'w') as f:            
            json.dump(self.__objects, f)

    def reload(self):
        """
        Quietly load the JSON back into a python object.
        """
        try:
            with open(self.__file_path, 'r') as f:
                py_obj = json.load(f)
                self.__objects.update(py_obj)
            return py_obj
        except:
            pass
