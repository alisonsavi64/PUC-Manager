from application.usecases.includeRegister.IncludeRegister import includeRegister
from application.usecases.listRegisters.ListRegisters import ListRegisters
from application.usecases.deleteRegister.deleteRegister import deleteRegister
from application.usecases.updateRegister.updateRegister import updateRegister
from Domain.entities.Teacher import Teacher

class TeacherController:
    def __init__(self, repository):
        self.repository = repository.createTeacherRepository()
    
    def create(self):
        print('\n----- INCLUSÃO -----\n')
        teacherCode = input('Insira o código do professor: ')
        teacherName = input('Insira o nome do professor: ')
        teacherCPF = input('Insira o cpf do professor: ')
        includeRegisterUseCase = includeRegister(self.repository)
        if(teacherCode == '' and teacherName == '' and teacherCPF == ''): return
        includeRegisterUseCase.execute(Teacher(teacherCode, teacherName, teacherCPF))

    def list(self):
        print('\n ----- LISTA DE PROFESSORES -----\n')
        listRegistersUseCase = ListRegisters(self.repository)
        professores = listRegistersUseCase.execute()
        for index, professor in enumerate(professores):
            print(f"\n - [{index + 1}] Código: [{professor['code']}] Nome: {professor['name']} CPF: {professor['cpf']}")

    def delete(self):
        idToDelete = input('Escolha um indice da lista para ser deletado: ')
        deleteRegistersUseCase = deleteRegister(self.repository)
        deleteRegistersUseCase.execute(idToDelete)

    def update(self):
        idToDelete = input('Escolha um indice da lista para ser atualizado: ')
        teacherCode = input('Insira o código do professor: ')
        teacherName = input('Insira o nome do professor: ')
        teacherCPF = input('Insira o cpf do professor: ')
        if(teacherCode == '' and teacherName == '' and teacherCPF == ''): return
        deleteRegistersUseCase = updateRegister(self.repository)
        deleteRegistersUseCase.execute(Teacher(teacherCode, teacherName, teacherCPF), idToDelete)