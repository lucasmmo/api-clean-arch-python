"""
to delete some commentary we need id and repository of this commentary
"""
class DeleteCommentary:
    def __init__(self, commentary_id, repository):
        self.commentary_id = commentary_id
        self.repository = repository

    def delete_commentary_of_database(self):
        self.repository.delete(self.commentary_id)

