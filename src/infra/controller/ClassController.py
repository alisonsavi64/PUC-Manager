from application.usecases.includeRegister.IncludeRegister import includeRegister
from application.usecases.listRegisters.ListRegisters import ListRegisters
from application.usecases.deleteRegister.deleteRegister import deleteRegister
from application.usecases.updateRegister.updateRegister import updateRegister
from Domain.entities.Class import Class

class ClassController:
    def __init__(self, repository):
        self.repository = repository.createClassRepository()

    def create(self):
        print('\n----- INCLUSÃO -----\n')
        classCode = input('Insira o código da turma: ')
        disciplineCode = input('Insira o código da disciplina: ')
        teacherCode = input('Insira o código do professor: ')
        if(teacherCode == '' and disciplineCode == '' and classCode == ''): return
        includeRegisterUseCase = includeRegister(self.repository)
        includeRegisterUseCase.execute(Class(classCode, teacherCode, disciplineCode))

    def list(self):
        print('\n ----- LISTA DE TURMAS -----\n')
        listRegistersUseCase = ListRegisters(self.repository)
        classes = listRegistersUseCase.execute()
        for index, classData in enumerate(classes):
            print(f"\n - [{index + 1}] Código: [{classData['code']}] Disciplina: {classData['disciplineCode']} Professor: {classData['teacherCode']}")
        
    def delete(self):
        idToDelete = input('Escolha um indice da lista para ser deletado: ')
        deleteRegistersUseCase = deleteRegister(self.repository)
        deleteRegistersUseCase.execute(idToDelete)

    def update(self):
        idToDelete = input('Escolha um indice da lista para ser atualizado: ')
        classCode = input('Insira o novo código da turma: ')
        disciplineCode = input('Insira o novo código da disciplina: ')
        teacherCode = input('Insira o novo código do professor: ')
        if(teacherCode == '' and disciplineCode == '' and classCode == ''): return
        deleteRegistersUseCase = updateRegister(self.repository)
        deleteRegistersUseCase.execute(Class(classCode, teacherCode, disciplineCode), idToDelete)
