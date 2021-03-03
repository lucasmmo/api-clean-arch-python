"""
this class is a repository that have methods to made some connections in database
here we need access in database
"""
class CategoryRepository:
    categories = []
    def __init__(self):
        pass
    
    def save(self, category):
        for category in categories:
            if category == category:
                return
            self.categories.append(category)
    
    def load(self, category_id):
        for category in categories:
            if category['category_id'] == category_id:
                return category
            return None

    def delete(self, category_id):
        for category in categories:
            if category['category_id'] == category_id:
                return category
            return None
        

