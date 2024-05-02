from infra.Repository.DatabaseRepository.StudentRepository import StudentRepository
from infra.Repository.DatabaseRepository.TeacherRepository import TeacherRepository
from infra.Repository.DatabaseRepository.ClassRepository import ClassRepository
from infra.Repository.DatabaseRepository.EnrollmentRepository import EnrollmentRepository
from infra.Repository.DatabaseRepository.DisciplineRepository import DisciplineRepository

#Repositorio Master que cria e fornece todos os outros repositorios 

class MemoryRepositoryFactory:
    def __init__(self):
        self.studentRepository = StudentRepository()
        self.teacherRepository = TeacherRepository()
        self.classRepository = ClassRepository()
        self.enrollmentRepository = EnrollmentRepository()
        self.disciplineRepository = DisciplineRepository()

    #Deleta todos os valores de todos os repositorios
    def deleteAll(self):
        self.studentRepository.deleteAll()
        self.teacherRepository.deleteAll()
        self.classRepository.deleteAll()
        self.enrollmentRepository.deleteAll()
        self.disciplineRepository.deleteAll()

    #Retorna o repositorio de estudantes
    def createStudentRepository(self):
        return self.studentRepository
    
    #Retorna o repositorio de professores
    def createTeacherRepository(self):
        return self.teacherRepository

    #Retorna o repositorio de turmas
    def createClassRepository(self):
        return self.classRepository

    #Retorna o repositorio de matriculas
    def createEnrollmentRepository(self):
        return self.enrollmentRepository

    #Retorna o repositorio de disciplinas
    def createDisciplineRepository(self):
        return self.disciplineRepository
