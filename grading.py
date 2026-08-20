class Grade:
    def __init__(self, students, professors, courses):
        self.students = students
        self.professors = professors
        self.courses = courses
        self.grades = {}

    def assign_grade(self, professor_id, student_id, course_code, grade):
        professor = self.professors.get(professor_id)
        student = self.students.get(student_id)
        course = self.courses.get(course_code)

        if not professor or not student or not course:
            return False, "Student, professor or course not found"

        if course.code not in student.registered_courses:
            return False, "Student is not registered in the course"

        if professor.user_id != course.professor_id:
            return False, "Professor does not teach this course"
        
        valid_grades = ["A", "B", "C", "D", "F"]

        if grade not in valid_grades:
            return False, "Invalid grade"

        if student.user_id not in self.grades:
            self.grades[student.user_id] = {}

        self.grades[student.user_id][course.code] = grade

        student.completed_courses[course.code] = grade

        return True, "Grade added"

    def calculate_gpa(self, student_id):
        student = self.students.get(student_id)

        if not student:
            return 0.0
        
        grade_points = {"A": 4.0,"B": 3.0,"C": 2.0,"D": 1.0,"F": 0.0}
        total_credit_hours = 0
        total_grade_points = 0

        for course_code, grade in student.completed_courses.items():
            course = self.courses.get(course_code)

            if course:
                points = grade_points.get(grade, 0)
                total_credit_hours += course.credit_hours
                total_grade_points += points * course.credit_hours

        if total_credit_hours == 0:
            return 0.0

        return total_grade_points / total_credit_hours

    def get_student_gpa(self, student_id):
        return self.calculate_gpa(student_id)

    def get_course_grades(self, course_code):
        course_grades = []

        for student in self.students.values():
            if course_code in student.completed_courses:

                course_grades.append({"id": student.user_id,"name": student.name,"grade": student.completed_courses[course_code]})
        return course_grades

    def class_average_gpa(self):
        total = 0
        count = 0

        for student in self.students.values():
            gpa = self.calculate_gpa(student.user_id)

            if gpa > 0:
                total += gpa
                count += 1

        if count == 0:
            return 0.0

        return total / count