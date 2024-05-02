from application.usecases.includeStudent.IncludeStudent import includeStudent
from application.usecases.listStudents.ListStudents import ListStudents
from Domain.entities.Student import Student

#Controller que cria e executa os useCases de estudantes
class StudentController:
    def __init__(self, repository):
        self.repository = repository

    #Cria um estudante
    def create(self, student):
        includeStudentUseCase = includeStudent(self.repository)
        includeStudentUseCase.execute(Student(student))

    #Lista os estudantes
    def list(self):
        listStudentsUseCase = ListStudents(self.repository)
        listStudentsUseCase.execute()
