class Students:
    def __init__(self):
        self.students=[]
    def add_student(self,n,c,cr,t='08:00'):
        self.students.append({'name':n,'contact_info':c,'course':cr,'preferred_time':t})
    def remove_student(self,n):
        self.students=[s for s in self.students if s['name']!=n]
    def get_students(self):
        return self.students
