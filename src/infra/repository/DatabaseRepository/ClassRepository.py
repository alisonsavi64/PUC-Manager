import json, os
    
class ClassRepository:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.classes = json.load(database)
    
    def save(self, classData):
        self.open_database()
        self.classes['classes'].append({'code': classData.code, 'teacherCode': classData.teacherCode, 'disciplineCode': classData.disciplineCode})
        self._save_to_file()
    
    def getAll(self):
        self.open_database()
        return self.classes['classes']
    
    def delete(self, id):
        self.open_database()
        if(int(id) > len(self.classes['classes'])): return
        del self.classes['classes'][int(id) - 1]
        self._save_to_file()
    
    def update(self, classData, id):
        self.open_database()
        if(int(id) > len(self.classes['classes'])): return
        self.classes['classes'][int(id) - 1] = {'code': classData.code, 'teacherCode': classData.teacherCode, 'disciplineCode': classData.disciplineCode}
        self._save_to_file()
    
    def open_database(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.classes = json.load(database)

    def _save_to_file(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')
        with open(database_path, 'w') as database:
            json.dump(self.classes, database, indent=4)
            