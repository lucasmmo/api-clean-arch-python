"""
to load some category we need the id of category and repository
"""
class LoadCategoryInteractor:
    def __init__(self, repository):
        self.repository = repository

    def load_category_of_database(self, category_id):
       try:
            return self.repository.load(category_id)
        except:
            print("Error On LoadCategoryInteractor")