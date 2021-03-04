"""
this class is a repository that have methods to made some connections in database
here we need access in database
"""
class UserRepository:
    def __init__(self):
        pass
    
    def save(self, user):
        print(f'This user {user} was save in database')

    def load(self, user_id):
        return user_id

    def delete(self, user_id):
        return True