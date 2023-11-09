#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    Initializes a new User instance.

    Parameters:
    - email (str): User's email (default is an empty string).
    - password (str): User's password (default is an empty string).
    - first_name (str): User's first name (default is an empty string).
    - last_name (str): User's last name (default is an empty string).
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
