#!/usr/bin/python3

from  models.base_model import BaseModel

class City(BaseModel):
    """
    Initializing a new City

    Paramets:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """
    state_id: str = ""
    name: str = ""

    def to_dict(self):
        """
        Return dictionary representation of City class.
        """
        city_dict = super().to_dict()
        city_dict['state_id'] = self.state_id
        city_dict['name'] = self.name
        return city_dict
