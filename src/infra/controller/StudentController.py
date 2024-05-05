from application.usecases.includeRegister.IncludeRegister import includeRegister
from application.usecases.listRegisters.ListRegisters import ListRegisters
from application.usecases.deleteRegister.deleteRegister import deleteRegister
from Domain.entities.Student import Student

class StudentController:
    def __init__(self, repository):
        self.repository = repository.createStudentRepository()

    def create(self):
        print('\n----- INCLUSÃO -----\n')
        studentName = input('Insira o nome do estudante: ')
        studentCode = input('Insira o código do estudante: ')
        includeRegisterUseCase = includeRegister(self.repository)
        if(studentName != '' and studentCode != ''): includeRegisterUseCase.execute(Student(studentName, studentCode))

    def list(self):
        print('\n ----- LISTA DE ESTUDANTES -----\n')
        listRegistersUseCase = ListRegisters(self.repository)
        estudantes = listRegistersUseCase.execute()
        for index, estudante in enumerate(estudantes):
            print(f"\n - [{index + 1}] [{estudante['code']}] {estudante['name']}")

    def delete(self):
        idToDelete = input('Escolha um indice da lista para ser deletado: ')
        deleteRegistersUseCase = deleteRegister(self.repository)
        deleteRegistersUseCase.execute(idToDelete)