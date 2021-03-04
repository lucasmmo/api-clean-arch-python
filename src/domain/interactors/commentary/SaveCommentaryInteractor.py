"""
to save a commentary we need a commentary and some repository to access the db
"""
class SaveCommentaryInteractor:
    def __init__(self, repository):
        self.repository = repository
    
    def save_commentary_on_database(self, commentary):
        try:
            self.repository.save(commentary)
        except:
            print("Error on SaveCommentaryInteractor")
        