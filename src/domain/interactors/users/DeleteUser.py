"""
to delete some user we need id and repository of this user
"""
class DeleteUser:
    def __init__(self, user_id, repository):
        self.user_id = user_id
        self.repository = repository

    def delete_user_of_database(self):
        self.repository.delete(self.user_id)

