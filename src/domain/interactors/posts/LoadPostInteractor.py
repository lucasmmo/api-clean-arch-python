"""
to load some post we need the id of post and repository
"""
class LoadPostInteractor:
    def __init__(self, repository):
        self.repository = repository

    def load_post_of_database(self, post_id):
        try:
            return self.repository.load(post_id)
        except:
            print("Error On LoadPostInteractor")