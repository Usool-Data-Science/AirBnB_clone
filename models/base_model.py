#!/usr/bin/python3
import uuid
import models
import datetime
"""
import storage
A module that declares the blueprint for our objects.
"""


class BaseModel():
    """
    A blueprint for all our objects.
    """
    def __init__(self, *args, **kwargs):
        """Instantiate the class with its attributes"""
        if kwargs:
            # If keyword args are given first declare these first
            self.id = kwargs['id']
            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            self.created_at = datetime.datetime.strptime(
                kwargs['created_at'], fmt)
            self.updated_at = datetime.datetime.strptime(
                kwargs['updated_at'], fmt)
            # Then declare others
            for k, v in kwargs.items():
                if k not in [
                        '__class__', 'id', 'created_at', 'updated_at']:
                    setattr(self, k, v)
        # If there is no keyword argument, then create only these 2
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Prints an unofficial representation of the class"""
        return("[{}] ({}) {}".format(
               self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """Return official representation of the object."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
            self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at
           with current datetime. If the object is newly created,
           update it using the storage.new() method and pass the
           instance of that object to it
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
           of __dict__ of the instance
        """
        dico = self.__dict__
        dico.update({'__class__': self.__class__.__name__})
        dico['created_at'] = str(self.created_at.isoformat())
        if 'update_at' in dico:
            dico['updated_at'] = str(self.updated_at.isoformat())
        else:
            now = datetime.datetime.now()
            dico['updated_at'] = str(now.isoformat())

        return dico
