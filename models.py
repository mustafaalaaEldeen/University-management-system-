import math

class User:
    def __init__(self, user_id, name, password):
        self.user_id = user_id
        self.name = name
        self.password = password

    def login(self, password):
        return self.password == password

class Student(User):
    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password)

        self.registered_courses = []
        self.completed_courses = {}
       
    def calculate_gpa(self, courses):
        grade_points = {"A": 4.0,"B": 3.0,"C": 2.0,"D": 1.0,"F": 0.0}
        total_points = 0
        total_hours = 0

        for code, grade in self.completed_courses.items():
            course = courses.get(code)

            if course:
                points = grade_points.get(grade, 0)
                total_points += points * course.credit_hours
                total_hours += course.credit_hours

        if total_hours == 0:
            return 0.0

        gpa = total_points / total_hours
        return math.floor(gpa * 100) / 100 

class Professor(User):

    def __init__(self, user_id, name, password):
        super().__init__(user_id, name, password)

        self.assigned_courses = []

    def assign_grade(self, student, course_code, grade):
        correct_grades = ["A", "B", "C", "D", "F"]

        if grade not in correct_grades:
            return False, "Invalid grade"

        student.completed_courses[course_code] = grade
        return True, "Grade added successfully"
     
class Course:
    def __init__(self,code,name,credit_hours,capacity,prerequisites=None,professor_id=None):
        self.code = code
        self.name = name
        self.credit_hours = credit_hours
        self.capacity = capacity
        self.prerequisites = prerequisites or []
        self.registered_students = []
        self.professor_id = professor_id

    def is_available(self):
        return len(self.registered_students) < self.capacity

    def available_seats(self):
        return self.capacity - len(self.registered_students)   