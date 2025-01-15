def get_grade(total_mark: float) -> str:
    """
    Determine the grade based on the total mark.

    Parameters:
    total_mark (float): The total mark obtained.

    Returns:
    str: The corresponding grade.

    Grading Scale:
    - A+: 90-100
    - A: 85-89
    - A-: 80-84
    - B+: 75-79
    - B: 70-74
    - B-: 65-69
    - C+: 60-64
    - C: 50-59
    - C-: 45-49
    - D: 40-44
    - F: 0-39
    - NG: Not Graded (if mark is outside 0-100)

    Example:
    >>> get_grade(92)
    'A+'
    >>> get_grade(67)
    'B-'

    """
    if total_mark <= 100 and total_mark >= 90:
        grade = "A+"
    elif total_mark < 90 and total_mark >= 85:
        grade = "A"
    elif total_mark < 85 and total_mark >= 80:
        grade = "A-"
    elif total_mark < 80 and total_mark >= 75:
        grade = "B+"
    elif total_mark < 75 and total_mark >= 70:
        grade = "B"
    elif total_mark < 70 and total_mark >= 65:
        grade = "B-"
    elif total_mark < 65 and total_mark >= 60:
        grade = "C+"
    elif total_mark < 60 and total_mark >= 50:
        grade = "C"
    elif total_mark < 50 and total_mark >= 45:
        grade = "C-"
    elif total_mark < 45 and total_mark >= 40:
        grade = "D"
    elif total_mark < 40 and total_mark >= 0:
        grade = "F"
    else:
        grade = "NG"
    return grade

print("Students's mark is 80 and the grade is : ",get_grade(80))
print(get_grade(50))
print(get_grade(30))
#print(get_grade())