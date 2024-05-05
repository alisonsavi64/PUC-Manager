import json, os

class EnrollmentRepository:
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')        
        with open(database_path, 'r') as database:
            self.enrollments = json.load(database)
    
    def save(self, enrollment):
        self.enrollments['enrollments'].append({'studentCode': enrollment.studentCode, 'classCode': enrollment.classCode})
        self._save_to_file()
    
    def getAll(self):
        return self.enrollments['enrollments']
    
    def delete(self, id):
        del self.enrollments['enrollments'][id - 1]
        self._save_to_file()
    
    def _save_to_file(self):
        current_dir = os.path.dirname(__file__)
        database_path = os.path.join(current_dir, 'database.json')
        with open(database_path, 'w') as database:
            json.dump(self.enrollments, database, indent=4)
