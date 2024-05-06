import json, os

class StudentRepository:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.students = json.load(database)
    
    def save(self, student):
        self.open_database()
        self.students['students'].append({'name': student.name, 'code': student.code})
        self._save_to_file()
    
    def getAll(self):
        self.open_database()
        return self.students['students']
    
    def delete(self, id):
        self.open_database()
        if(int(id) > len(self.students['students'])): return
        del self.students['students'][int(id) - 1]
        self._save_to_file()
    
    def update(self, student, id):
        self.open_database()
        if(int(id) > len(self.students['students'])): return
        self.students['students'][int(id) - 1] = {'name': student.name, 'code': student.code}
        self._save_to_file()
    
    def open_database(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.students = json.load(database)

    def _save_to_file(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')
        with open(database_path, 'w') as database:
            json.dump(self.students, database, indent=4)

    