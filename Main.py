from Data import format_data
from Google_API import get_results

results = get_results('Class Test','credentials.json')

questions = {
    'name': 'Name',
    'course': 'Class Ranking'
}

students,courses = format_data(results,questions)
x = 1