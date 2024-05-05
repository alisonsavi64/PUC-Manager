class deleteRegister:
    def __init__(self, repository):
        self.repository = repository
    
    def execute(self, index):
        return self.repository.delete(index)