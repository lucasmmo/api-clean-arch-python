"""
to save a new user we need a User and some repository to access the db
"""

class SaveUserInteractor:
    def __init__(self, repository):
        self.repository = repository
    
    def save_user_on_database(self, user):
        try:
            self.repository.save(user)
        except:
            print("Error on SaveUserInteractor")
        