import uuid # generate id
from datetime import datetime # get the current date and time
"""
BaseModel is a super class, it contains common attributes
"""
class BaseModel: 
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update updated_at timestamp"""
        self.updated_at = datetime.now()

    def update(self, data: dict):
        """Update attributes safely"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
