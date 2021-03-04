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
