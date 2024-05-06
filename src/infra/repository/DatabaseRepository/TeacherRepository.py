import json, os 

class TeacherRepository:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.teachers = json.load(database)
    
    def save(self, teacher):
        self.open_database()
        self.teachers['teachers'].append({'name': teacher.name, 'code': teacher.code, 'cpf': teacher.cpf})
        self._save_to_file()
    
    def getAll(self):
        self.open_database()
        return self.teachers['teachers']
    
    def delete(self, id):
        self.open_database()
        if(int(id) > len(self.teachers['teachers'])): return
        del self.teachers['teachers'][int(id) - 1]
        self._save_to_file()
    
    def update(self, teacher, id):
        self.open_database()
        if(int(id) > len(self.teachers['teachers'])): return
        self.teachers['teachers'][int(id) - 1] = {'name': teacher.name, 'code': teacher.code, 'cpf': teacher.cpf}
        self._save_to_file()

    def open_database(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.teachers = json.load(database)

    def _save_to_file(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')
        with open(database_path, 'w') as database:
            json.dump(self.teachers, database, indent=4)