"""
to instance this class we need the SaveUserInteractor to do the save 
"""

class SaveUserController:
    def __init__(self, interactor, user):
        self.interactor = interactor
        self.user = user
    
    def handle(self):
        try:
            self.interactor.save_user_on_database(self.user)
        except:
            print("Error On SaveUserController")
