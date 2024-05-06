#Alison Fracasso Savi - Análise e Desenvolvimento de Sitemas

#Arquivo principal que executa o código
from Domain.entities.MainMenuOptions import MainMenuOptions
from infra.controller.StudentController import StudentController
from infra.controller.DisciplineController import DisciplineController
from infra.controller.EnrollmentController import EnrollmentController
from infra.controller.TeacherController import TeacherController
from infra.controller.ClassController import ClassController
from infra.repository.DatabaseRepositoryFactory import DatabaseRepositoryFactory

#Variável que armazena o estado do Menu de Opções
mainMenu = True
#Variável que armazena o estado do Menu de Operações
operacionalMenu = False

#Repositório Master que cria todas as estruturas de impressão e armazenamento de entidades (Estudantes, Professores...)
RepositoryFactory = DatabaseRepositoryFactory()

#Inicialização do controller de estudantes
studentsController = StudentController(RepositoryFactory)
disciplinesController = DisciplineController(RepositoryFactory)
classesController = ClassController(RepositoryFactory)
enrollmentsController = EnrollmentController(RepositoryFactory)
teachersController = TeacherController(RepositoryFactory)

controllers = {
    "1": studentsController,
    "2": teachersController,
    "3": disciplinesController,
    "4": classesController,
    "5": enrollmentsController
}

#Bloco principal de execução
while mainMenu or operacionalMenu:
    
    if(mainMenu and not operacionalMenu):
        #Menu Principal
        print('----- MENU PRINCIPAL -----\n')
        print('(1) Gerenciar estudantes.')
        print('(2) Gerenciar professores.')
        print('(3) Gerenciar disciplinas.')
        print('(4) Gerenciar turmas.')
        print('(5) Gerenciar matrículas.')
        print('(9) Sair.\n')
        managementInput = input("Informe a opção desejada: ")
        if(managementInput == '9'): break
        if(managementInput not in ('1', '2', '3', '4', '5', '9')): continue
        operacionalMenu = True
    
    if(operacionalMenu):
        print(f'\n***** [{MainMenuOptions[managementInput]}] MENU DE OPERAÇÕES *****\n')
        print('(1) Incluir.')
        print('(2) Listar.')
        print('(3) Atualizar.')
        print('(4) Excluir.')
        print('(9) Voltar ao menu principal.\n')
        operationalInput = input("Informe a ação desejada: ")
        if(operationalInput == '9'): 
            operacionalMenu = False
        if(operationalInput == '1'):
            controllers[managementInput].create()
            continue
        if(operationalInput == '2'): 
            controllers[managementInput].list()
            continue
        if(operationalInput == '4'): 
            controllers[managementInput].delete()
            continue
        if(operationalInput == '3'): 
            controllers[managementInput].update()
            continue
print('\n===== ATUALIZAÇÃO =====\n')
print('Finalizando aplicação...')
