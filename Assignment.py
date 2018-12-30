import random

def assign_students(students,courses):
    student_names = list(students.keys())
    random.shuffle(student_names)

    for name in student_names:
        place_student(name,students[name],courses)


def place_student(name,student_preferences,courses):
    for course_name in student_preferences:
        if courses[course_name].is_full() is False:
            courses[course_name].add_student(name)
            return
        else:
            pass

    raise Exception('Student could not be assigned to any course')