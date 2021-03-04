"""
to instance this class we need the SaveCategoryInteractor to do the save 
"""

class SaveCategoryController:
    def __init__(self, interactor, category):
        self.interactor = interactor
        self.category = category
    
    def handle(self):
        try:
            self.interactor.save_category_on_database(self.category)
        except:
            print("Error On SaveCategoryController")
