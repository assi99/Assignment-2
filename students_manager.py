import json
class StudentsManager:
    def __init__(self, file_path='students.json'):
        self.file_path=file_path
        self.students=self.load_students()
    def load_students(self):
        try:
            with open(self.file_path,'r',encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return [
                {'name':'Alice','email':'alice@example.com','course':'Computer Science','preferred_time':'08:00'},
                {'name':'Bob','email':'bob@example.com','course':'Mathematics','preferred_time':'09:00'},
                {'name':'Charlie','email':'charlie@example.com','course':'Physics','preferred_time':'07:30'}
            ]
    def add_student(self,name,email,course,preferred_time='08:00'):
        self.students.append({'name':name,'email':email,'course':course,'preferred_time':preferred_time})
        self.save_students()
    def remove_student(self,name):
        self.students=[s for s in self.students if s['name']!=name]
        self.save_students()
    def save_students(self):
        with open(self.file_path,'w',encoding='utf-8') as f:
            json.dump(self.students,f,indent=4)
    def get_students(self):
        return self.students
    def list_students(self):
        for s in self.students:
            print(f"Name: {s['name']}, Email: {s['email']}, Course: {s['course']}, Preferred Time: {s['preferred_time']}")
