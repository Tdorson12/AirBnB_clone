#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def to_dict(self):
        """
        Return dictionary representation of User class.
        """
        user_dict = super().to_dict()
        user_dict['email'] = 'User.email'
        user_dict['password'] = self.password
        user_dict['first_name'] = self.first_name
        user_dict['last_name'] = self.last_name
        return user_dict
