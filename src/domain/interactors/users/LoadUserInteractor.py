"""
to load some user we need the id of user and repository
"""
class LoadUserInteractor:
    def __init__(self, repository):
        self.repository = repository

    def load_user_of_database(self, user_id):
        try:
            return self.repository.load(user_id)
        except:
            print("Error On LoadUserInteractor")
