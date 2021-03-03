"""
to save a commentary we need a commentary and some repository to access the db
"""

class SaveCommentary:
    def __init__(self, commentary, repository):
        self.commentary = commentary
        self.repository = repository
    
    def save_commentary_on_database(self):
        self.repository.save(self.commentary)

        