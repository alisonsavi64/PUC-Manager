import json, os

class EnrollmentRepository:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.enrollments = json.load(database)
    
    def save(self, enrollment):
        self.open_database()
        self.enrollments['enrollments'].append({'studentCode': enrollment.studentCode, 'classCode': enrollment.classCode})
        self._save_to_file()
    
    def getAll(self):
        self.open_database()
        return self.enrollments['enrollments']
    
    def delete(self, id):
        self.open_database()
        if(int(id) > len(self.enrollments['enrollments'])): return
        del self.enrollments['enrollments'][int(id) - 1]
        self._save_to_file()
    
    def update(self, enrollment, id):
        self.open_database()
        if(int(id) > len(self.enrollments['enrollments'])): return
        self.enrollments['enrollments'][int(id) - 1] = {'studentCode': enrollment.studentCode, 'classCode': enrollment.classCode}
        self._save_to_file()

    def open_database(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.enrollments = json.load(database)

    def _save_to_file(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')
        with open(database_path, 'w') as database:
            json.dump(self.enrollments, database, indent=4)
