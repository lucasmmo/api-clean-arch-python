"""
Category is the entity of program that is responsable only to made category
id(int)
name(str)
description(str)
creator(User)
up(int)
created_at(Date)
updated_at(Date)
"""
class Category:
    def __init__(self, category_id, name, description, creator, up=0, created_at, updated_at):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.creator = creator
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def category_id(self):
        return self._category_id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description
    
    @property
    def creator(self):
        return self._creator

    @property
    def created_at(self):
        return self._created_at
    
    @property
    def updated_at(self):
        return self._updated_at
    