#Classe que executa a inserção de um estudante
class includeStudent:
    def __init__(self, repository):
        self.studentRepository = repository.createStudentRepository()

    def execute(self, student):
        #Salva um estudante
        self.studentRepository.save(student)
         