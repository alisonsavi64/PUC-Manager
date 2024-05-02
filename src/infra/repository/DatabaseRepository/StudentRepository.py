import json

class StudentRepository:
    def __init__(self):
        with open('database.json', 'r') as database:
            self.students = json.load(database)['students']
    
    #Salva um estudante
    def save(self, student):
        self.students.append(student)
    
    #Retorna todos os estudantes
    def getAll(self):
        return self.students
    
    #Deleta todos os estudantes
    def deleteAll(self):
        self.students = []

    