"""
to save a post we need a post and some repository to access the db
"""
class SavePostInteractor:
    def __init__(self, repository):
        self.repository = repository
    
    def save_post_on_database(self, post):
        try:
            self.repository.save(post)
        except:
            print("Error on SavePostInteractor")

        