"""
to instance this class we need the SaveCommentaryInteractor to do the save 
"""
class SaveCommentaryController:
    def __init__(self, interactor):
        self.interactor = interactor
    
    def handle(self, commentary_id):
        try:
            self.interactor.save_commentary_on_database(commentary_id)
        except:
            print("Error On SaveCommentaryController")
