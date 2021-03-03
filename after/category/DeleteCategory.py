"""
to delete some category we need id and repository of this category
"""
class DeleteCategory:
    def __init__(self, category_id, repository):
        self.category_id = category_id
        self.repository = repository

    def delete_category_of_database(self):
        self.repository.delete(self.category_id)

