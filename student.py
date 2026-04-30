from course import Course

class Student:
    
    student_id = 0
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []
        self.student_id = Student.student_id
        Student.student_id += 1
    
    def __str__(self):
        course_str = ""
        for course in self.courses:
            course_str += str(course) + ", "
        if course_str:
            course_str = course_str[:-2]  # remove last comma and space
        return f"{self.first_name} {self.last_name}: {course_str}"
        
    def get_first_name(self):
        return self.first_name
        
    def get_last_name(self):
        return self.last_name
        
    def get_student_id(self):
        return self.student_id
    
    def add_course(self, new_course):
        self.courses.append(new_course)