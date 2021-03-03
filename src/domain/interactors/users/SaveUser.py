"""
to save a new user we need a User and some repository to access the db
"""

class SaveUser:
    def __init__(self, user, repository):
        self.user = user
        self.repository = repository
    
    def save_user_on_database(self):
        self.repository.save(self.user)

        