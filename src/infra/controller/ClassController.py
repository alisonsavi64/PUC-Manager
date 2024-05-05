from application.usecases.includeRegister.IncludeRegister import includeRegister
from application.usecases.listRegisters.ListRegisters import ListRegisters
from application.usecases.deleteRegister.deleteRegister import deleteRegister
from Domain.entities.Class import Class

class ClassController:
    def __init__(self, repository):
        self.repository = repository.createClassRepository()

    def create(self):
        print('\n----- INCLUSÃO -----\n')
        classCode = input('Insira o código da turma: ')
        disciplineCode = input('Insira o código da disciplina: ')
        teacherCode = input('Insira o código do professor: ')
        includeRegisterUseCase = includeRegister(self.repository)
        includeRegisterUseCase.execute(Class(classCode, teacherCode, disciplineCode))

    def list(self):
        print('\n ----- LISTA DE TURMAS -----\n')
        listRegistersUseCase = ListRegisters(self.repository)
        classes = listRegistersUseCase.execute()
        for index, classData in enumerate(classes):
            print(f"\n - [{index + 1}] Código: [{classData['classCode']}] {classData['disciplineCode']} {classData['teacherCode']}")
        
    def delete(self):
        idToDelete = input('Escolha um indice da lista para ser deletado: ')
        deleteRegistersUseCase = deleteRegister(self.repository)
        deleteRegistersUseCase.execute(idToDelete)