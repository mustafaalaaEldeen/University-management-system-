from datetime import date
class Attendance:

    def __init__(self, students, professors):
        self.students = students
        self.professors = professors
        self.attendance_record = {}

    def record_attendance(self,professor_id,student_id,course_code,attendance_status):
        professor = self.professors.get(professor_id)
        student = self.students.get(student_id)

        if not professor or not student:
            return False, "Wrong data"

        if course_code not in professor.assigned_courses:
            return False, "Professor does not teach this course"

        if course_code not in student.registered_courses:
            return False, "Student is not registered"

        if student.user_id not in self.attendance_record:
            self.attendance_record[student.user_id] = {}

        if course_code not in self.attendance_record[student.user_id]:
            self.attendance_record[student.user_id][course_code] = []

        attendance_date = date.today()

        self.attendance_record[student.user_id][course_code].append({"status": attendance_status,"date": attendance_date})

        return True, "Attendance saved"

    def get_attendance_percentage(self, student_id, course_code):

        if student_id not in self.attendance_record:
            return 0.0

        if course_code not in self.attendance_record[student_id]:
            return 0.0

        records = self.attendance_record[student_id][course_code]

        if not records:
            return 0.0

        present = 0

        for record in records:
            if record["status"]:
                present += 1

        return present / len(records) * 100