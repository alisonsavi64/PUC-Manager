#Alison Fracasso Savi - Análise e Desenvolvimento de Sitemas

#Arquivo principal que executa o código
from Domain.entities.MainMenuOptions import MainMenuOptions
from infra.Controller.StudentController import StudentController
from infra.Repository.MemoryRepositoryFactory import MemoryRepositoryFactory

#Variável que armazena o estado do Menu de Opções
mainMenu = True
#Variável que armazena o estado do Menu de Operações
operacionalMenu = False

#Repositório Master que cria todas as estruturas de impressão e armazenamento de entidades (Estudantes, Professores...)
memoryRepository = MemoryRepositoryFactory()

#Inicialização do controller de estudantes
studentsController = StudentController(memoryRepository)

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
        #Finalização da executação caso o valor inserido seja 9
        if(managementInput == '9'): break
        #Caso o valor de input seja diferente de 1 (Estudantes) printar EM DESENVOLVIMENTO
        if(managementInput != '1'): 
            print('\nEM DESENVOLVIMENTO\n')
            continue
        operacionalMenu = True
    
    if(operacionalMenu):
        #Bloco de execução das operações
        print(f'\n***** [{MainMenuOptions[managementInput]}] MENU DE OPERAÇÕES *****\n')
        print('(1) Incluir.')
        print('(2) Listar.')
        print('(3) Atualizar.')
        print('(4) Excluir.')
        print('(9) Voltar ao menu principal.\n')
        operationalInput = input("Informe a ação desejada: ")
        #Caso o valor do input seja 9 volta para o bloco do menu principal
        if(operationalInput == '9'): 
            operacionalMenu = False
        #Caso o valor do input seja 1 e executada a função de inclusão dos alunos
        if(operationalInput == '1'):
            print('\n----- INCLUSÃO -----\n')
            student = input('Insira o nome do estudante: ')
            if(student != ''): studentsController.create(student)
            continue
        #Caso o valor do input seja 1 e executada a função listagem dos alunos
        if(operationalInput == '2'): 
            studentsController.list()
            continue
        print('\nEM DESENVOLVIMENTO\n')

print('\n===== ATUALIZAÇÃO =====\n')
print('Finalizando aplicação...')

