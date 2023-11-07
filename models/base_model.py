#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """" This defines common attributes and methods for other classes """
    def __init__(self, *args, **kwargs):
        """ Initialize BaseModel instance. """
        if kwargs:
            """ if kwargs is not empty set attributes from kwargs """
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                    if key in ["created_at", "updated_at"]:
                        """ convert created_at and updated_at to datetime """
                        val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, val)
        else:
            """ if kwargs is empty generate the foll """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            """ Set update_at with the value of created_at """
            self.updated_at = self.created_at

    def __str__(self):
        """ Print [<class name>] (<self.id>) <self.__dict__> to the screen """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Update the updated_at to the current datetime """
        updated_at = datetime.utcnow()

    def to_dict(self):
        """ A dictionary containing all keys and values of the instance """
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": type(self).__name__
            }


if __name__ == "__main__":
    main()
