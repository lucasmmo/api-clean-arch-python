"""
to instance this class we need the LoadCommentaryInteractor to do the load 
"""
class LoadCommentaryController:
    def __init__(self, interactor):
        self.interactor = interactor
    
    def handle(self, commentary_id):
        try:
            return self.interactor.load_commentary_of_database(commentary_id)
        except:
            print("Error On LoadCommentaryController")