"""
this class is a repository that have methods to made some connections in database
here we need access in database
"""
class PostRepository:
    posts = []

    def __init__(self):
        pass
    
    def save(self, post):
        for post in posts:
            if post == post:
                return
            self.posts.append(post)
    
    def load(self, post_id):
        for post in posts:
            if post['post_id'] == post_id:
                return post
            return None

    def delete(self, post_id):
        for post in posts:
            if post['post_id'] == post_id:
                return post
            return None
        