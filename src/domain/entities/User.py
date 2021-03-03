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
    def __init__(self, user_id, name, last_name, age, email, password, privilaged=False, created_at, updated_at):
        self.user_id = user_id
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def last_name(self):
        return self._last_name
    
    @property
    def age(self):
        return self._age
    
    @property
    def email(self):
        return self._email
    
    @property
    def password(self):
        return self._password

        @property
    def created_at(self):
        return self._created_at
    
    @property
    def updated_at(self):
        return self._updated_at
    