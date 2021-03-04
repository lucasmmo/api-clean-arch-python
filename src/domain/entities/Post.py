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

    