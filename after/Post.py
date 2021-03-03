"""
Post is the entity of program that is responsable only to made posts
title(str)
body(str)
category(Category[])
creator(User)
up(int)
created_at(Date)
updated_at(Date)
"""
class Post:
    def __init__ (self, post_id, title, body, category, creator, up=0, created_at, updated_at):
        self.post_id = post_id
        self.title = title
        self.body = body
        self.category = category
        self.creator = creator
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def post_id(self):
        return self._post_id

    @property
    def title(self):
        return self._title
    
    @property
    def body(self):
        return self._body
    
    @property
    def category(self):
        return self._category
        
    @property
    def creator(self):
        return self._creator
    
    @property
    def up(self):
        return self._up
    
    @property
    def created_at(self):
        return self._created_at
    
    @property
    def updated_at(self):
        return self._updated_at
    