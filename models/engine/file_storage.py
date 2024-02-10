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
            print("Created at type in new: {}".format(type(obj.created_at)))
            self.__objects[key] = obj

    def save(self):
        """
        First convert all obj in the __object to dict, then
        dumps the __object dictionary into a JSON file.
        """
        with open(self.__file_path, 'w', encoding='UTF-8') as f:
            dico = {}
            for k,v in self.__objects.items():
                dico[k] = v.to_dict()
            json.dump(dico, f)

    def reload(self):
        """
        Quietly load the JSON back into a python object.
        """
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                py_obj = json.load(f)
                for k,v in py_obj.items():
                    '''
                    For each of the key in the JSON file, recreate
                    the BaseModel. **v indicates that we are passing
                    each of the value (BasedModel.__dict__) that we
                    previously saved as keyword args. If you forget
                    to add the ** it will import it all as string
                    which will affect the self.created_at and
                    self.updated_at attribute by not allowing it
                    to convert into datetime appropriately.
                    '''
                    self.__objects[k] = BaseModel(**v)
                    obj_check = self.__objects[k]
                    print("Create_at after import: {}".format(type(obj_check['created_at'])))
                return py_obj
        except Exception as e:
            pass

    def destroy(self, key):
        """Deletes a key from the storage"""
        del(self.__objects[key])
        dico = {}
        with open(self.__file_path, 'w') as f:
            for k, v in self.__objects.items():
                dico[k] = v.to_dict()
            json.dump(dico, f)

    def update(self, id_, key_, value_):
        """Updates a key with new value"""
        obj = self.__objects.get(id_)
        if obj:
            setattr(obj, key_, value_)
