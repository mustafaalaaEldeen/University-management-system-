from models import Student, Professor, Course

def create_sample_data():

    professors = {

        "PROF01": Professor("PROF01","Dr.Ahmed Yasser ","1234"),

        "PROF02": Professor("PROF02","Dr. Mona Mohamed","4321")
    }

    professors["PROF01"].assigned_courses = ["CCE112","CCE113"]

    professors["PROF02"].assigned_courses = ["CCE121"]

    students = {
        "STU01": Student("STU01","Mohamed Atia","1111"),

        "STU02": Student("STU02","Sara Mohamed","2222"),

        "STU03": Student("STU03","Youssef Ahmed","3333"),

        "STU04": Student("STU04","Aya Mohamed","4444")
    }

    students["STU01"].completed_courses = {"CCE112": "A"}

    courses = {

        "CCE112": Course("CCE112","Digital Logic Design",3,3,[],"PROF01"),

        "CCE121": Course("CCE121","Computer Programming",3,4,[],"PROF02"),

        "CCE113": Course("CCE113","Computer Architecture ",3,2,["CCE112"],"PROF01")
    }

    return students, professors, courses