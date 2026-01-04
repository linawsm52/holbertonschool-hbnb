import re  # used for validation
from .base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()

        # Validate first and last name
        self._validate_name(first_name, "first_name")
        self._validate_name(last_name, "last_name")

        # Validate email format
        self._validate_email(email)

        # Assign attributes
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

        # Relationship: a user can own multiple places
        self.places = []

    def _validate_name(self, value, field):
        """Check required and max 50 characters"""
        if not value or len(value) > 50:
            raise ValueError(f"{field} is required and max 50 characters")

    def _validate_email(self, email):
        """Validate standard email format"""
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, email):
            raise ValueError("Invalid email format")
