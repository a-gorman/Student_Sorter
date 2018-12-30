from Data import format_data
from Assignment import assign_students
from Google_API import get_results
from Output import courses_to_csv

results = get_results('Class Test','credentials.json')

questions = {
    'name': 'Name',
    'course': 'Class Ranking'
}

students,courses = format_data(results,questions,2)

assign_students(students,courses)

courses_to_csv(courses)