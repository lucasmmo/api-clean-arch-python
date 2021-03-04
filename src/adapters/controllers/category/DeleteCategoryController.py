"""
to instance this class we need the DeleteCategoryInteractor to do the delete 
"""
class DeleteCategoryController:
    def __init__(self, interactor, category_id):
        self.interactor = interactor
        self.category_id = category_id
    
    def handle(self):
        try:
            return self.interactor.delete_category_of_database(self.category_id)
        except:
            print("Error On DeleteCategoryController")