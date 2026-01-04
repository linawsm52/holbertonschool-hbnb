from app.models.user import User
from app.persistence.repository import InMemoryRepository

"""
HBnBFacade class connect models with Repository
"""

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

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

    # ===== Place =====
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass
