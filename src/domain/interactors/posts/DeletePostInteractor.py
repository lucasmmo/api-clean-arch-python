"""
to delete some post we need id and repository of this post
"""
class DeletePostInteractor:
    def __init__(self, repository):
        self.repository = repository

    def delete_post_of_database(self, post_id):
        try:
            return self.repository.delete(post_id)
        except:
            print("Error On DeletePostInteractor")

