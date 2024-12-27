# assessments 
quiz  = float(input("Quiz "))
test =  float(input("Test "))
mid =   float(input("Mid  "))
final = float(input("Final "))
total  = quiz + test + mid + final
if total <= 100 and total >= 90:
    grade ="A+"
elif total < 90 and total >= 85:
    grade ="A"
elif total < 85 and total >= 80:
    grade ="A-"
elif total < 80 and total >= 75:
    grade ="B+"
elif total < 75 and total >= 70:
    grade ="B"
elif total < 70 and total >= 65:
    grade ="B-"
elif total < 65 and total >= 60:
    grade ="C+"
elif total < 60 and total >= 50:
    grade ="C"
elif total < 50 and total >= 45:
    grade ="C-"
elif total < 45 and total >= 40:
    grade ="d"
elif total < 40 and total >= 0:
    grade ="F"
else:
    grade ="NG"
print("Grade : ", grade)