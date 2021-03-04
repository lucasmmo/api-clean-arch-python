"""
to save a category we need a category and some repository to access the db
"""

class SaveCategoryInteractor:
    def __init__(self, repository):
        self.repository = repository
    
    def save_category_on_database(self, category):
        try:
            self.repository.save(category)
        except:
            print("Error on SaveCategoryInteractor")
        