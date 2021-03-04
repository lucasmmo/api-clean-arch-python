"""
to delete some category we need id and repository of this category
"""
class DeleteCategoryInteractor:
    def __init__(self, repository):
        self.repository = repository

    def delete_category_of_database(self, category_id):
        try:
            return self.repository.delete(category_id)
        except:
            print("Error On DeleteCategoryInteractor")

