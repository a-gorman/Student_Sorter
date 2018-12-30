import re
from Course import Course

def format_data(table,questions,course_size):
    students, course_names = parse_data(table,questions)
    
    courses = {}
    for name in course_names:
        courses[name] = Course(name,course_size)

    return students,courses



def parse_data(table,questions):
    name_col_loc, courses = parse_header(table[0],questions)

    students = {}
    for row in table[1:]:
        name, pref = parse_row(row,name_col_loc,courses)
        students[name] = pref
    
    course_names = courses.values()

    return students,course_names


def parse_row(row,name_col_loc,courses):
    student_name = row[name_col_loc]


    course_preferences = [None] * len(courses)
    for i in range(len(row)):
        if i in courses:
            course_preferences[int(row[i])-1] = courses[i] # -1 due to answers being 1 indexed (first choice is choice #1)
        else:
            pass

    return student_name,course_preferences

def parse_header(header,questions):
    courses = {}
    for i in range(len(header)):
        if header[i] == questions['name']:
            name_col = i
        else:
            course_name = get_course_name(header[i],re.escape(questions['course']))
            if course_name is not None:
                courses[i] = course_name

    return name_col,courses


def get_course_name(cell,question):
    match = re.match(r'\A' + question + r' \[' + r'([\w ]+)' + r'\]',cell)
    if match is None:
        return None
    else:
        return match.group(1)

