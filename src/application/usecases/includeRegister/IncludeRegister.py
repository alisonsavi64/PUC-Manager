class includeRegister:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, input):
        self.repository.save(input)
