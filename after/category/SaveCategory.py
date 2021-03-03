"""
to save a category we need a category and some repository to access the db
"""

class SaveCategory:
    def __init__(self, category, repository):
        self.category = category
        self.repository = repository
    
    def save_category_on_database(self):
        self.repository.save(self.category)
        