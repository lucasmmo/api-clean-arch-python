"""
to delete some post we need id and repository of this post
"""
class DeletePost:
    def __init__(self, post_id, repository):
        self.post_id = post_id
        self.repository = repository

    def delete_post_of_database(self):
        self.repository.delete(self.post_id)

