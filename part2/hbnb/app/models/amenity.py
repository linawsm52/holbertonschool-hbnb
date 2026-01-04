from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()

        """must be maximum length of 50 character"""
        if not name or len(name) > 50:
            raise ValueError("Amenity name is required and max 50 characters")

        self.name = name
