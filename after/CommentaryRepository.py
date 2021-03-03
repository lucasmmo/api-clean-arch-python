"""
this class is a repository that have methods to made some connections in database
here we need access in database
"""
class CommentaryRepository:
    comentaries = []

    def __init__(self):
        pass
    
    def save(self, commentary):
        for commentary in comentaries:
            if commentary == commentary:
                return
            self.comentaries.append(commentary)
    
    def load(self, commentary_id):
        for commentary in comentaries:
            if commentary['commentary_id'] == commentary_id:
                return commentary
            return None

    def delete(self, commentary_id):
        for commentary in comentaries:
            if commentary['commentary_id'] == commentary_id:
                return commentary
            return None

