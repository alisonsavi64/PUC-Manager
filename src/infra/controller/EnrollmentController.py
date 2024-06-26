from application.usecases.includeRegister.IncludeRegister import includeRegister
from application.usecases.listRegisters.ListRegisters import ListRegisters
from application.usecases.deleteRegister.deleteRegister import deleteRegister
from application.usecases.updateRegister.updateRegister import updateRegister
from Domain.entities.Enrollment import Enrollment

class EnrollmentController:
    def __init__(self, repository):
        self.repository = repository.createEnrollmentRepository()

    def create(self):
        print('\n----- INCLUSÃO -----\n')
        studentCode = input('Insira o código do estudante: ')
        studentClass = input('Insira o código da turma: ')
        includeRegisterUseCase = includeRegister(self.repository)
        if(studentCode == '' and studentClass == ''): return
        includeRegisterUseCase.execute(Enrollment(studentCode, studentClass))

    def list(self):
        print('\n ----- LISTA DE MATRÍCULAS -----\n')
        listRegistersUseCase = ListRegisters(self.repository)
        matriculas = listRegistersUseCase.execute()
        for index, matricula in enumerate(matriculas):
            print(f"\n - [{index + 1}] Código: [{matricula['classCode']}] Estudante: {matricula['studentCode']}")   

    def delete(self):
        idToDelete = input('Escolha um indice da lista para ser deletado: ')
        deleteRegistersUseCase = deleteRegister(self.repository)
        deleteRegistersUseCase.execute(idToDelete)
    
    def update(self):
        idToDelete = input('Escolha um indice da lista para ser atualizado: ')
        studentCode = input('Insira o novo código do estudante: ')
        studentClass = input('Insira o novo código da turma: ')
        if(studentCode == '' and studentClass == ''): return
        deleteRegistersUseCase = updateRegister(self.repository)
        deleteRegistersUseCase.execute(Enrollment(studentCode, studentClass), idToDelete)