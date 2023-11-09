#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """"
        This defines common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
            Initialize BaseModel instance.
        """
        if kwargs:
            """
                if kwargs is not empty set attributes from kwargs
            """
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                    if key in ["created_at", "updated_at"]:
                        """
                            convert created_at and updated_at to datetime
                        """
                        val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, val)
        else:
            """
               if kwargs is empty generate the foll
            """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            """
                Set update_at with the value of created_at
            """
            self.updated_at = datetime.utcnow()
            """
            if it’s a new instance (not from a dictionary representation)
            add a call to the method new(self) on storage
            """
            storage.new(self)

    def __str__(self):
        """
            Print [<class name>] (<self.id>) <self.__dict__> to the screen
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the updated_at to the current datetime
        """
        updated_at = datetime.utcnow()
        self.updated_at = updated_at
        """ call save(self) method of storage """
        storage.save()

    def to_dict(self):
        """
        Return dictionary representation of BaseModel class.
        """
        self._dict = self.__dict__.copy()
        self._dict["id"] = self.id
        self._dict["created_at"] = self.created_at.isoformat()
        self._dict["updated_at"] = self.updated_at.isoformat()
        self._dict["__class__"] = self.__class__.__name__

        return self._dict
