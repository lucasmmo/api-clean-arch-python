"""
this class is a repository that have methods to made some connections in database
here we need access in database
"""
class PostRepository:
    def __init__(self):
        pass
    
    def save(self, post):
        print(f'This user {post} was save in database')

    def load(self, post_id):
        return post_id

    def delete(self, post_id):
        return True
        