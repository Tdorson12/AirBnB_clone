#!/usr/bin/python3

from models.base_model import BaseModel
from typing import List


class Place(BaseModel):
    """
    Initializing the class

    Parameters:
    city_id: string - empty string: it will be the City.id
    user_id: string - empty string: it will be the User.id
    name: string - empty string
    description: string - empty string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of string - empty list: it will be the list of Amenity.id later
    """
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: List[str] = []

    def to_dict(self):
        """
        Return dictionary representation of Place class.
        """
        place_dict = super().to_dict()
        place_dict['city_id'] = self.city_id
        place_dict['user_id'] = self.user_id
        place_dict['name'] = self.name
        place_dict['description'] = self.description
        place_dict['number_rooms'] = self.number_rooms
        place_dict['number_bathrooms'] = self.number_bathrooms
        place_dict['max_guest'] = self.max_guest
        place_dict['price_by_night'] = self.price_by_night
        place_dict['latitude'] = self.latitude
        place_dict['longitude'] = self.longitude
        place_dict['amenity_ids'] = self.amenity_ids
        return place_dict

