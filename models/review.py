#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Initializing the class

    Parameters:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""

    def to_dict(self):
        """
        Return dictionary representation of Review class.
        """
        review_dict = super().to_dict()
        review_dict['place_id'] = self.place_id
        review_dict['user_id'] = self.user_id
        review_dict['text'] = self.text
        return review_dict
