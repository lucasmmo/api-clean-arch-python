"""
to load some post we need the id of post and repository
"""
class LoadPost:
    def __init__(self, post_id, repository)
        self.post_id = post_id
        self.repository = repository

    def load_post_of_database(self):
        loaded_post = self.repository.load(post_id)
        if loaded_post:
            return loaded_post
        return "Doesn't have any post with this id"