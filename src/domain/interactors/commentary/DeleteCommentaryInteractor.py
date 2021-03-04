"""
to delete some commentary we need id and repository of this commentary
"""
class DeleteCommentaryInteractor:
    def __init__(self, repository):
        self.repository = repository

    def delete_commentary_of_database(self, commentary_id):
        try:
            return self.repository.delete(commentary_id)
        except:
            print("Error On DeleteCommentaryInteractor")
