class RegistrationSystem:
    def __init__(self, students, courses):
        self.students = students
        self.courses = courses

    def check_prerequisites(self, student, course):
        for prereq in course.prerequisites:

            if prereq not in student.completed_courses:
                return False

            if student.completed_courses[prereq] == "F":
                return False

        return True

    def register(self, student_id, course_code):
        student = self.students.get(student_id)
        course = self.courses.get(course_code)

        if not student:
            return False, "Student not found"

        if not course:
            return False, "Course not found"

        if course.code in student.registered_courses:
            return False, student.name + " is already registered in " + course.code
        
        if not course.is_available():
            return False, course.code + " is full. Capacity: " + str(course.capacity)
        
        if not self.check_prerequisites(student, course):

            not_completed = []

            for prereq in course.prerequisites:

                if prereq not in student.completed_courses:
                    not_completed.append(prereq)

                elif student.completed_courses[prereq] == "F":
                    not_completed.append(prereq + " (F)")

            return False, student.name + " is not completed prerequisites: " + str(not_completed)
       
        student.registered_courses.append(course.code)
        course.registered_students.append(student.user_id)

        return True, "Registration successful"

    def unregister(self, student_id, course_code):
        student = self.students.get(student_id)
        course = self.courses.get(course_code)

        if not student or not course:
            return False, "Student or course not found"

        if course.code not in student.registered_courses:
            return False, "Student is not registered"

        student.registered_courses.remove(course.code)

        if student.user_id in course.registered_students:
            course.registered_students.remove(student.user_id)
        return True, "Unregistered successfully"

    def get_available_courses(self):
        available = []

        for course in self.courses.values():

            if course.is_available():
                available.append(course)

        return available   