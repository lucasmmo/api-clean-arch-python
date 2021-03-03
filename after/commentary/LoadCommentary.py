"""
to load some commentary we need the id of commentary and repository
"""
class LoadCommentary:
    def __init__(self, commentary_id, repository)
        self.commentary_id = commentary_id
        self.repository = repository

    def load_commentary_of_database(self):
        loaded_commentary = self.repository.load(commentary_id)
        if loaded_commentary:
            return loaded_commentary
        return "Doesn't have any commentary with this id"