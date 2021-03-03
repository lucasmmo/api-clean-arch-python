"""
to save a post we need a post and some repository to access the db
"""

class SavePost:
    def __init__(self, post, repository):
        self.post = post
        self.repository = repository
    
    def save_post_on_database(self):
        self.repository.save(self.post)

        