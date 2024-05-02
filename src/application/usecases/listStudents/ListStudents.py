#Classe que executa a listagem dos estudantes
class ListStudents:
    def __init__(self, repository):
        self.studentRepository = repository.createStudentRepository()

    def execute(self):
        #Função que retorna todos os estudantes
        students = self.studentRepository.getAll()
        print('\n ----- LISTA DE ESTUDANTES -----\n')
        for student in students:
            print(f'\n - {student.name}')
         