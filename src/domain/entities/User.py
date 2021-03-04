"""
User is the entity of program that is responsable only to made users
name(str)
last_name(str)
age(int)
email(str)
password(str)
privilaged(bool)=False
created_at(Date)
updated_at(Date)
"""
class User:
    def __init__(self, user_id, name, last_name, age, email, password, privilaged, created_at, updated_at):
        self.user_id = user_id
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at
