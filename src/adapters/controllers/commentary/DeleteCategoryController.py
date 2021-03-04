"""
to instance this class we need the DeleteCommentaryInteractor to do the delete 
"""
class DeleteCommentaryController:
    def __init__(self, interactor):
        self.interactor = interactor
    
    def handle(self, commentary_id):
        try:
            return self.interactor.delete_commentary_of_database(commentary_id)
        except:
            print("Error On DeleteCommentaryController")