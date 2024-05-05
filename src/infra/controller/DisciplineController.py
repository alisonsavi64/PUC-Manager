from application.usecases.includeRegister.IncludeRegister import includeRegister
from application.usecases.listRegisters.ListRegisters import ListRegisters
from application.usecases.deleteRegister.deleteRegister import deleteRegister
from Domain.entities.Discipline import Discipline

class DisciplineController:
    def __init__(self, repository):
        self.repository = repository.createDisciplineRepository()

    def create(self):
        print('\n----- INCLUSÃO -----\n')
        disciplineName = input('Insira o nome da disciplina: ')
        disciplineCode = input('Insira o código da disciplina: ')
        includeRegisterUseCase = includeRegister(self.repository)
        includeRegisterUseCase.execute(Discipline(disciplineCode, disciplineName))

    def list(self):
        print('\n ----- LISTA DE DISCIPLINAS -----\n')
        listRegistersUseCase = ListRegisters(self.repository)
        disciplinas = listRegistersUseCase.execute()
        for index, disciplina in enumerate(disciplinas):
            print(f"\n - [{index + 1}] Código: [{disciplina['code']}] {disciplina['name']}")

    def delete(self):
        idToDelete = input('Escolha um indice da lista para ser deletado: ')
        deleteRegistersUseCase = deleteRegister(self.repository)
        deleteRegistersUseCase.execute(idToDelete)