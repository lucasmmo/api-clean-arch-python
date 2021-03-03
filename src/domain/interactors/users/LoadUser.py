"""
to load some user we need the id of user and repository
"""
class LoadUser:
    def __init__(self, user_id, repository)
        self.user_id = user_id
        self.repository = repository

    def load_user_of_database(self):
        loaded_user = self.repository.load(user_id)
        if loaded_user:
            return loaded_user
        return "Doesn't have any user with this id"