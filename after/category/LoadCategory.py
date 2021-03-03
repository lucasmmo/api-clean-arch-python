"""
to load some category we need the id of category and repository
"""
class LoadCategory:
    def __init__(self, category_id, repository)
        self.category_id = category_id
        self.repository = repository

    def load_category_of_database(self):
        loaded_category = self.repository.load(category_id)
        if loaded_category:
            return loaded_category
        return "Doesn't have any category with this id"