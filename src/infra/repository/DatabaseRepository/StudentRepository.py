import json, os

class StudentRepository:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.students = json.load(database)
    
    def save(self, student):
        self.students['students'].append({'name': student.name, 'code': student.code})
        self._save_to_file()
    
    def getAll(self):
        return self.students['students']
    
    def delete(self, id):
        del self.students['students'][id - 1]
        self._save_to_file()

    def _save_to_file(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')
        with open(database_path, 'w') as database:
            json.dump(self.students, database, indent=4)

    