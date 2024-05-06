import json, os

class DisciplineRepository:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.disciplines = json.load(database)
    
    def save(self, discipline):
        self.open_database()
        self.disciplines['disciplines'].append({'name': discipline.name, 'code': discipline.code})
        self._save_to_file()
    
    def getAll(self):
        self.open_database()
        return self.disciplines['disciplines']
    
    def delete(self, id):
        self.open_database()
        if(int(id) > len(self.disciplines['disciplines'])): return
        del self.disciplines['disciplines'][int(id) - 1]
        self._save_to_file()

    def update(self, discipline, id):
        self.open_database()
        if(int(id) > len(self.disciplines['disciplines'])): return
        self.disciplines['disciplines'][int(id) - 1] = {'name': discipline.name, 'code': discipline.code}
        self._save_to_file()
    
    def open_database(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.disciplines = json.load(database)

    def _save_to_file(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')
        with open(database_path, 'w') as database:
            json.dump(self.disciplines, database, indent=4)
    