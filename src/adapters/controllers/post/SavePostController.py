"""
to instance this class we need the SavePostInteractor to do the save 
"""

class SavePostController:
    def __init__(self, interactor, post):
        self.interactor = interactor
        self.post = post
    
    def handle(self):
        try:
            self.interactor.save_post_on_database(self.post)
        except:
            print("Error On SavepostController")
