from .base_model import BaseModel
from .user import User
from .place import Place

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()

        """Required string"""
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Review text is required")

        """must be int between 1 and 5"""
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        """ensure the place exists"""
        if not isinstance(place, Place):
            raise ValueError("place must be a Place instance")

        """ensure the user exists"""
        if not isinstance(user, User):
            raise ValueError("user must be a User instance")

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

        place.add_review(self) # to add the review to the place
