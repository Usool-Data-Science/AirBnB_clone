#!/usr/bin/python3
"""
A command line module that handles user request.
"""
import cmd
import models

#classes = {'BaseModel':models.base_model.BaseModel,
#           'FileStorage':models.engine.file_storage}

class HBNBCommand(cmd.Cmd):
    """
    A blueprint for our command line interface.
    """
    prompt = "(hbnb) "
    classes = ['BaseModel', 'FileStorage']
    def do_create(self, line):
        """Creates a new instance of BaseModel,
           saves it and then print it's ID.
        """
        if not line:
            print('** class name missing **')
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            model = models.base_model.BaseModel()
            model.save()
            print(model.id)
    
    def do_show(self, line):
        """Prints the unofficial form of an object"""
        line = self.parseline(line)[-1].split(" ")
        # If there is no args, i.e. parseline gives ['']
        if not line[0]:
            print("** class name missing **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif len(line) >= 1 and line[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            key = '.'.join([line[0], line[1]])
            storage = models.storage.all()
            obj = storage.get(key)
            if obj:
                print(obj)
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        line = self.parseline(line)[-1].split(" ")
        if not line[0]:
            print("** class name missing **")
        elif len(line) == 1:
            if line[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(line) >= 1 and line[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            key = '.'.join([line[0], line[1]])
            storage = models.storage
            try:
                storage.destroy(key)
            except KeyError as err:
                print("** no instance found **")

    def do_quit(self, line):
        """Handle the quit command"""
        return True

    def do_EOF(self, line):
        """
        Handles end of line cases.
        """
        return True

    def postloop(self):
        """
        Prints empty line before exiting the command line.
        """
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
