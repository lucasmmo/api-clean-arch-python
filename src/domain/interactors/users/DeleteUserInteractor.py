"""
to delete some user we need id and repository of this user
"""
class DeleteUserInteractor:
    def __init__(self, repository):
        self.repository = repository

    def delete_user_of_database(self, user_id):
        try:
            return self.repository.delete(user_id)
        except:
            print("Error On DeleteUserInteractor")
