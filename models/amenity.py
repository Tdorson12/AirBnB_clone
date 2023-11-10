#!/usr/bin/python3

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    Initializing the class

    Parameters:
    name: string - empty string
    """
    name: str = ""

    def to_dict(self):
        """
        Return dictionary representation of Amenity class.
        """
        amenity_dict = super().to_dict()
        amenity_dict['name'] = self.name
        return amenity_dict

