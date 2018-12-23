import re
from dataclasses import dataclass


def parse_data(table,questions):
    name_col, course_names = parse_header(table[1],questions)
    


def parse_header(header,questions):
    courses = {}
    for i in range(header):
        if header[i] == questions['name']:
            name_col = i
        else:
            course_name = get_course_name(header[i],questions['course'])
            if course_name is not None:
                courses[course_name] = i

    return name_col,courses


def get_course_name(cell,question):
    match = re.match(r'\A' + question + r' \[' + r'([\w ]+)' + r'\]',cell)
    if match is None:
        return None
    else:
        return match.group(1)