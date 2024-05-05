import json, os 

class TeacherRepository:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.teachers = json.load(database)
    
    def save(self, teacher):
        self.teachers['teachers'].append({'name': teacher.name, 'code': teacher.code, 'cpf': teacher.cpf})
        self._save_to_file()
    
    def getAll(self):
        return self.teachers['teachers']
    
    def delete(self, id):
        del self.teachers['teachers'][id - 1]
        self._save_to_file()

    def _save_to_file(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')
        with open(database_path, 'w') as database:
            json.dump(self.teachers, database, indent=4)