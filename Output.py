def courses_to_csv(courses):
    string = 'Course\n'
    for course in courses:
        string = string + courses[course].to_csv() + '\n'

    output_file = open('Output.csv','w')
    output_file.write(string)
    output_file.close()