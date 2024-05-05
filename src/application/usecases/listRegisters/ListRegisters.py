#Classe que executa a listagem dos estudantes
class ListRegisters:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        return self.repository.getAll()