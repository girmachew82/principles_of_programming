# initialization
course_title = "Principles of Programming" #in double quote
course_code = 'SEng 2021' # in single quote
year ="""2""" # in triple quote
semester ='''I'''# in triple quote

print('Course title:', " ",course_title) # concatinate by comma
print('Course code:'+ " "+course_code)  # concatinate by +
print(f'Year: {year}')# print by f-string
print("Semester: {}".format(semester)) # print by format method with placeholder
print("================================================================")
format_string = "Course title: {0}\nCourse code: {1} \nYear: {2}\nSemester: {3}".format(course_title, course_code,year,semester)
print(format_string)