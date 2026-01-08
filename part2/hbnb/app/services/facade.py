from app.models.user import User # user model 
from app.models.amenity import Amenity # amenity model
from app.persistence.repository import InMemoryRepository # srorage

"""
HBnBFacade class connect models with Repository
and handles CRUD
"""

class HBnBFacade:
    def __init__(self):
        self.user = {}
        self.place = {}
        self.review = {}
        self.amenity = {}

    # ===== User =====
    def create_user(self, user_data):
        """
        create user object
        and save it to memory
        return the new user object
        """
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """
        return user by id
        none otherwise 
        """
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """
        return user by email
        """
        return self.user_repo.get_by_attribute('email', email)
        """
        get_by_attribute is InMemoryRepository function
        """

    def get_all_users(self):
        """
        return all users object
        """
        return self.user_repo.get_all()

    def update_user(self, user_id, data):
        """
        update user info
        """
        user = self.get_user(user_id)
        if not user:
            return None
        user.update(data)
        return user
    
    # ===== Amenity  =====
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None
        amenity.update(amenity_data)
        return amenity

facade = HBnBFacade() #object to call its methods
