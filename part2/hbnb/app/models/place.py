from .base_model import BaseModel
from .user import User

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()

        """Required, maximum length of 100 characters."""
        if not title or len(title) > 100:
            raise ValueError("Title is required and max 100 characters")

        """Must be a positive value"""
        if price <= 0:
            raise ValueError("Price must be positive")

        """Must be within the range of -90.0 to 90.0"""
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude out of range")

        """Must be within the range of -180.0 to 180.0"""
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude out of range")

        """ensure the owner exists"""
        if not isinstance(owner, User):
            raise ValueError("Owner must be a User instance")

        self.title = title
        self.description = description
        self.price = float(price)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.owner = owner

        self.reviews = []     # one-to-many
        self.amenities = []   # many-to-many

    def add_review(self, review):
        self.reviews.append(review)
        self.save()

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)
            self.save()
