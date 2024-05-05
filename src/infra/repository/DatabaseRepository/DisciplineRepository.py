import json, os

class DisciplineRepository:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.disciplines = json.load(database)
    
    def save(self, discipline):
        self.disciplines['disciplines'].append({'name': discipline.name, 'code': discipline.code})
        self._save_to_file()
    
    def getAll(self):
        return self.disciplines['disciplines']
    
    def delete(self, id):
        del self.disciplines['disciplines'][id - 1]
        self._save_to_file()

    def _save_to_file(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')
        with open(database_path, 'w') as database:
            json.dump(self.disciplines, database, indent=4)
    