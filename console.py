#!/usr/bin/python3

import cmd
#from models import storage
#import models
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HolbertonBnB project.

    Attributes:
    - prompt (str): The command prompt.

    Methods:
    - do_EOF: Exit the program gracefully on EOF.
    - do_quit: Exit the program gracefully using the "quit" command.
    - emptyline: Handle an empty line (do nothing).
    """

    prompt = "(hbnb) "
    _classes = ["BaseModel"]

    def do_EOF(self, line):
        """
        Exit the program gracefully on EOF.
        """
        return True

    def do_quit(self, line):
        """
        Exit the program gracefully using the "quit" command.

        Usage: quit
        """
        return True

    def emptyline(self):
        """
        Handle an empty line (do nothing).
        """
        pass

    def do_create(self, line):
        """
        Create a new instance of BaseModel and save it to the JSON file.

        Usage: create <class_name>
        """
        if not line:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(line)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        Show a string representation of an instance

        Usage: show <class_name> <id>
        """
        if not line:
            print("** class name missing **")
        else:
            try:
                class_name, _id = line.split(" ")
            except ValueError:
                print("** instance id missing **")
            else:
                all_objects = storage.all()
                if class_name in self._classes:
                    instance_key = f"{class_name}.{_id}"
                    if instance_key in all_objects:
                        print(all_objects[instance_key])
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Delete an instance base on the class name and id

        Usage: destroy <class_name> <id>
        """
        if not line:
            print("** class name missing **")
        else:
            try:
                class_name, _id = line.split(" ")
            except ValueError:
                print("** instance id missing **")
            else:
                all_objects = storage.all()
                if class_name not in self._classes:
                    print("** class doesn't exist **")
                else:
                    instance_key = f"{class_name}.{_id}"
                    if instance_key in all_objects:
                        del all_objects[instance_key]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name

        Usage: all <class_name> or all
        """
        all_objects = storage.all()
        if line not in self._classes:
            print("** class doesn't exist **")
        else:
            result = []
            for obj_key, obj in all_objects.items():
                if not line or obj_key.startswith(line + "."):
                    result.append(str(obj))

            print(result)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split(" ")
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0].strip()
            if class_name in self._classes:
                if len(args) >= 2:
                    _id = args[1].strip()
                    all_object = storage.all()
                    instance_key = f"{class_name}.{_id}"
                    if instance_key in all_object:
                        if len(args) >= 3:
                            attribute_name = args[2].strip()
                            if len(args) >= 4:
                                attribute_value_str = " ".join(args[3:]).strip('\"')
                                instance = all_object[instance_key]

                                try:
                                    attribute_value = eval(attribute_value_str)
                                except (NameError, SyntaxError):
                                    attribute_value = attribute_value_str

                                setattr(instance, attribute_name, attribute_value)
                                instance.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
