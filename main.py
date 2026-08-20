from data_manager import DataManager
from sample_data import create_sample_data
from registration import RegistrationSystem
from grading import Grade
from attendance import Attendance

def student_menu(student, registration, grading, attendance, dm, professors):

    while True:

        print("\n===== Student Menu =====")
        print("1. Available Courses")
        print("2. Register Course")
        print("3. Unregister Course")
        print("4. My Courses")
        print("5. My Grades")
        print("6. My Attendance")
        print("7. Logout")

        choice = input("Choose: ")
        
        if choice == "1":
            courses = registration.get_available_courses()

            if not courses:
                print("No courses available.")

            else:
                print("\nAvailable Courses:")

                for course in courses:
                    print(course.code ,"-" , course.name ," - Hours: " ,course.credit_hours ," - Seats: " ,course.available_seats())
        
        elif choice == "2":
            code = input("Course Code: ")

            result, message = registration.register(student.user_id,code)
            print(message)

            if result:
                dm.save_all(registration.students,professors,registration.courses)
        
        elif choice == "3":
            code = input("Course Code: ")

            result, message = registration.unregister(student.user_id,code)
            print(message)

            if result:
                dm.save_all(registration.students,professors,registration.courses)
        
        elif choice == "4":
            print("\nMy Courses:")

            if not student.registered_courses:
                print("You are not registered in any course.")

            else:
                for code in student.registered_courses:
                    course = registration.courses.get(code)

                    if course:
                        print(course.code , "-" , course.name)
        
        elif choice == "5":
            print("\nMy Grades:")

            if not student.completed_courses:
                print("No grades available.")

            else:
                for code, grade in student.completed_courses.items():
                    print(code , "-" , grade)

                print("GPA:",grading.get_student_gpa(student.user_id))
        
        elif choice == "6":
            print("\nMy Attendance:")

            student_records = attendance.attendance_record.get(student.user_id)

            if not student_records:
                print("No attendance records.")

            else:
                for code in student_records:
                    percentage = attendance.get_attendance_percentage(student.user_id,code)

                    print(code , "-" , percentage , "%")
        
        elif choice == "7":
            print("Logged out successfully.")
            break

        else:
            print("Wrong choice")

def professor_menu(professor, grading, attendance, dm):

    while True:

        print("\n===== Professor Menu =====")
        print("1. My Courses")
        print("2. Enter Grade")
        print("3. Record Attendance")
        print("4. Course Grades")
        print("5. Logout")

        choice = input("Choose: ")
        
        if choice == "1":
            print("\nMy Courses:")

            if not professor.assigned_courses:
                print("No courses.")

            else:
                for code in professor.assigned_courses:
                    course = grading.courses.get(code)

                    if course:
                        print(course.code , " - " , course.name)
        
        elif choice == "2":
            student_id = input("Student ID: ")
            course_code = input("Course Code: ")
            grade = input("Enter student grade: ")

            result, message = grading.assign_grade(professor.user_id,student_id,course_code,grade)
            print(message)

            if result:
                dm.save_all(grading.students,grading.professors,grading.courses)
        
        elif choice == "3":
            student_id = input("Student ID: ")
            course_code = input("Course Code: ")

            answer = input(
                "Is the student present? (t/f): ")
            present = answer == "t"

            result, message = attendance.record_attendance(professor.user_id,student_id,course_code,present)
            print(message)

            if result:
                dm.save_all(attendance.students,attendance.professors,grading.courses)
        
        elif choice == "4":
            course_code = input("Course Code: ") 

            report = grading.get_course_grades(course_code)

            if not report:
                print("No grades available.")

            else:
                print("\nCourse Grades:")

                for student in report:
                    print(student["id"] , "-" , student["name"] , "-" ,student["grade"])

                print("Average GPA:",grading.class_average_gpa())
        
        elif choice == "5":
            print("Logged out successfully.")
            break

        else:
            print("Wrong choice")

def main():
    dm = DataManager()

    students = dm.load_students()
    professors = dm.load_professors()
    courses = dm.load_courses()

    if not students and not professors and not courses:
        print("Initializing system")

        students, professors, courses = create_sample_data()

        dm.save_all(students,professors,courses)

    registration = RegistrationSystem(students,courses)

    grading = Grade(students,professors,courses)

    attendance = Attendance(students,professors)

    while True:
        
        print("\n===== University Management System =====")               
        print("1. Student Login")
        print("2. Professor Login")
        print("3. Exit")

        choice = input("Choose: ")
        
        if choice == "1":
            user_id = input("Student ID: ")
            password = input("Password: ")

            student = students.get(user_id)

            if student and student.login(password):

                print("\nWelcome," , student.name)
                student_menu(student,registration,grading,attendance,dm,professors)

            else:
                print("Invalid ID or password")
        
        elif choice == "2":

            user_id = input("Professor ID: ")
            password = input("Password: ")

            professor = professors.get(user_id)

            if professor and professor.login(password):

                print("\nWelcome, " , professor.name)
                professor_menu(professor,grading,attendance,dm)

            else:
                print("Invalid ID or password")
        
        elif choice == "3":
            print("Thank you for using the system")
            break

        else:
            print("Invalid option")
main()