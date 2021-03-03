"""
Commentary is the entity of program that is responsable only to made Commentary
commentary(str)
creator(User)
post(Post)
up(int)
created_at(Date)
updated_at(Date)
"""
class Commentary:
    def __init__(self, commentary_id, commentary, creator, post, up=0, created_at, updated_at):
        self.commentary_id = commentary_id
        self.commentary = commentary
        self.creator = creator
        self.post = post
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def commentary_id(self):
        return self._commentary_id
        
    @property
    def commentary(self):
        return self._commentary
    
    @property
    def creator(self):
        return self._creator
    
    @property
    def post(self):
        return self._post
    
    @property
    def up(self):
        return self._up
    
    @property
    def created_at(self):
        return self._created_at
    
    @property
    def updated_at(self):
        return self._updated_at
