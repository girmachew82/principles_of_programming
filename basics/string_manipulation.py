hello = "Hello World\n"
print(hello * 3)
print(hello[0])
print(hello[-1])
print(hello[-2])
print(hello[0:5])
hello[0] = 'h'#string is immutable error
course_title = '''This is principles of programming'''
#check in string

print("SEng in ",course_title,  ' = ','SEng' in course_title , end=" ")
print("\n===============================")
print("seng in ", course_title, ' = ', 'Seng' in course_title)
print('Sng in ', course_title, ' = ', 'Sng' in course_title)
print('SEng not in ', course_title, ' = ','SEng' not in course_title)
for s in course_title:
    print(s)

