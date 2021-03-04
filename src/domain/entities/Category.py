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

    