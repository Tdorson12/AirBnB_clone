#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
