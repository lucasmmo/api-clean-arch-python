"""
to load some commentary we need the id of commentary and repository
"""
class LoadCommentaryInteractor:
    def __init__(self, repository):
        self.repository = repository

    def load_commentary_of_database(self, commentary_id):
        try:
            return self.repository.load(commentary_id)
        except:
            print("Error On LoadCommentaryInteractor")