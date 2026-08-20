import os
from models import Student, Professor, Course

class DataManager:

    def load_students(self):
        students = {}

        if not os.path.exists("students.txt"):
            return students

        with open("students.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(",")
                    user_id = data[0]
                    name = data[1]
                    password = data[2]
                    student = Student(user_id,name,password)
                    if len(data) > 3 and data[3]:
                        student.registered_courses = data[3].split(";")
                    if len(data) > 4 and data[4]:
                        completed_items = data[4].split(";")
                        for item in completed_items:
                            if ":" in item:
                                c_code, grade = item.split(":")
                                student.completed_courses[c_code] = grade

                    students[user_id] = student

        return students

    def save_students(self, students):
        with open("students.txt", "w") as file:
            for student_id, student in students.items():
                reg_courses_str = ";".join(student.registered_courses)

                comp_courses_list = []
                for code, grade in student.completed_courses.items():
                    comp_courses_list.append(code + ":" + grade)

                comp_courses_str = ";".join(comp_courses_list)

                line = (
                    student.user_id
                    + ","
                    + student.name
                    + ","
                    + student.password
                    + ","
                    + reg_courses_str
                    + ","
                    + comp_courses_str
                    + "\n"
                )

                file.write(line)

        print("Students data saved successfully.")

    def load_professors(self):
        professors = {}

        if not os.path.exists("professors.txt"):
            return professors

        with open("professors.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(",")
                    user_id = data[0]
                    name = data[1]
                    password = data[2]

                    professor = Professor(user_id,name,password)

                    if len(data) > 3 and data[3]:
                        professor.assigned_courses = data[3].split(";")

                    professors[user_id] = professor

        return professors

    def save_professors(self, professors):
        with open("professors.txt", "w") as file:
            for prof_id, professor in professors.items():
                assigned_str = ";".join(professor.assigned_courses)

                line = (
                    professor.user_id
                    + ","
                    + professor.name
                    + ","
                    + professor.password
                    + ","
                    + assigned_str
                    + "\n"
                )

                file.write(line)

        print("Professors data saved successfully.")

    def load_courses(self):
        courses = {}

        if not os.path.exists("courses.txt"):
            return courses

        with open("courses.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(",")
                    code = data[0]
                    name = data[1]
                    credit_hours = int(data[2])
                    capacity = int(data[3])

                    prereqs = []

                    if len(data) > 4 and data[4]:
                        prereqs = data[4].split(";")

                    prof_id = None

                    if len(data) > 5 and data[5] != "None":
                        prof_id = data[5]

                    course = Course(code,name,credit_hours,capacity,prereqs,prof_id)

                    if len(data) > 6 and data[6]:
                        course.registered_students = data[6].split(";")

                    courses[code] = course

        return courses

    def save_courses(self, courses):

        with open("courses.txt", "w") as file:
            for code, course in courses.items():
                prereqs_str = ";".join(course.prerequisites)

                prof_id_str = "None"
                if course.professor_id:
                    prof_id_str = course.professor_id

                reg_students_str = ";".join(course.registered_students)

                line = (
                    course.code
                    + ","
                    + course.name
                    + ","
                    + str(course.credit_hours)
                    + ","
                    + str(course.capacity)
                    + ","
                    + prereqs_str
                    + ","
                    + prof_id_str
                    + ","
                    + reg_students_str
                    + "\n"
                )

                file.write(line)

        print("Courses data saved successfully.")

    def save_all(self, students, professors, courses):

        self.save_students(students)
        self.save_professors(professors)
        self.save_courses(courses)