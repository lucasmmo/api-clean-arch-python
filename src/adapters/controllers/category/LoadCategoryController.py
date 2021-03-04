"""
to instance this class we need the LoadCategoryInteractor to do the load 
"""
class LoadCategoryController:
    def __init__(self, interactor, category_id):
        self.interactor = interactor
        self.category_id = category_id
    
    def handle(self):
        try:
            return self.interactor.load_category_of_database(self.category_id)
        except:
            print("Error On LoadCategoryController")