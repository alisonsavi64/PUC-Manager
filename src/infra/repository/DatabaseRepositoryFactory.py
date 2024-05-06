from infra.repository.DatabaseRepository.StudentRepository import StudentRepository
from infra.repository.DatabaseRepository.TeacherRepository import TeacherRepository
from infra.repository.DatabaseRepository.ClassRepository import ClassRepository
from infra.repository.DatabaseRepository.EnrollmentRepository import EnrollmentRepository
from infra.repository.DatabaseRepository.DisciplineRepository import DisciplineRepository

class DatabaseRepositoryFactory:
    def __init__(self):
        self.studentRepository = StudentRepository()
        self.teacherRepository = TeacherRepository()
        self.classRepository = ClassRepository()
        self.enrollmentRepository = EnrollmentRepository()
        self.disciplineRepository = DisciplineRepository()

    def createStudentRepository(self):
        return self.studentRepository
    
    def createTeacherRepository(self):
        return self.teacherRepository

    def createClassRepository(self):
        return self.classRepository

    def createEnrollmentRepository(self):
        return self.enrollmentRepository

    def createDisciplineRepository(self):
        return self.disciplineRepository
