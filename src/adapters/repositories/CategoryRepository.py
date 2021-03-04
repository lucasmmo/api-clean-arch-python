"""
this class is a repository that have methods to made some connections in database
here we need access in database
"""
class CategoryRepository:
    def __init__(self):
        pass
    
    def save(self, category):
        print(f'This user {category} was save in database')

    def load(self, category_id):
        return category_id

    def delete(self, category_id):
        return True
        

