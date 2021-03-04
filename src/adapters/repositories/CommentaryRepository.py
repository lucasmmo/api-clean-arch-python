"""
this class is a repository that have methods to made some connections in database
here we need access in database
"""
class CommentaryRepository:
    def __init__(self):
        pass
    
    def save(self, commentary):
        print(f'This user {commentary} was save in database')

    def load(self, commentary_id):
        return commentary_id

    def delete(self, commentary_id):
        return True

