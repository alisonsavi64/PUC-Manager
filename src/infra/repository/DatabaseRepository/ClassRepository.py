import json, os
    
class ClassRepository:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.classes = json.load(database)
    
    def save(self, classData):
        self.classes['classes'].append({'code': classData.code, 'teacherCode': classData.teacherCode, 'disciplineCode': classData.disciplineCode})
        self._save_to_file()
    
    def getAll(self):
        return self.classes['classes']
    
    def delete(self, id):
        del self.classes['classes'][id - 1]
        self._save_to_file()

    def _save_to_file(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')
        with open(database_path, 'w') as database:
            json.dump(self.classes, database, indent=4)
            