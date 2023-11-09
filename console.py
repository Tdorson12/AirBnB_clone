#!/usr/bin/python3

import cmd


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

    def do_EOF(self, line):
        """
        Exit the program gracefully on EOF.
        """
        return True

    def do_quit(self, line):
        """
        Exit the program gracefully using the "quit" command.
        """
        return True

    def emptyline(self):
        """
        Handle an empty line (do nothing).
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
