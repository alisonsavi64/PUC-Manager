class updateRegister:
    def __init__(self, repository):
        self.repository = repository
    
    def execute(self, input, index):
        if(index not in ('1', '2', '3', '4', '5', '6', '7', '8', '9')): return
        return self.repository.update(input, index)