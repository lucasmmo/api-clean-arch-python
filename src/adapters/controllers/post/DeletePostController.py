"""
to instance this class we need the DeletePostInteractor to do the delete 
"""
class DeletePostController:
    def __init__(self, interactor, post_id):
        self.interactor = interactor
        self.post_id = post_id
    
    def handle(self):
        try:
            return self.interactor.delete_post_of_database(self.post_id)
        except:
            print("Error On DeletePostController")