
course_title = "Principles of Programming" #in double quote
course_code = 'SEng 2021' # in single quote
year ="""2""" # in triple quote
semester ='I'# in triple quote

print('Course Title\t\t\t Course Code\t Year\t Semester\t')
print(course_title,'\t',course_code,'\t', year, '\t', semester,'\t')
print("This is principles of programming course in pyhton.\nIt\'s in second year course\nIt\'s for Software Engineering students")
txt = "Hello\nWorld!"
print(txt) 
txt = "Hello\rWorld!"
print(txt) 
txt = "Hello \bWorld!"
print(txt) 
#A backslash followed by three integers will result in a octal value:
txt = "\110\141\154\154\157"
print(txt) 
txt = "\101\102\103\104\105"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x61\x6c\x6c\x6f"
print(txt) 