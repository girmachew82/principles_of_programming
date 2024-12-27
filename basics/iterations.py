for i in range(1, 11):
    print(f'Number {i}')
# sum of the first 10 integers
sum = 0
for i in range(1, 11):
    sum += i
print(f'Sum  = {sum}')

# Total mark
lab_exam  = 15
test  = 15
project = 30
final_exam = 40
total_mark = lab_exam + test + project + final_exam
print('Lab exam = ' , lab_exam)
print('Test = ', test)
print('Project = ', project)
print('Final exam = ', final_exam)
print('Total mark = ', total_mark)
total_assessment = [lab_exam, test, project, final_exam]