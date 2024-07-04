def calculate_grade(score):
    if score >=90:
        grade = 'A'
    elif score >=80:
        grade = 'B'
    elif score >=70:
        grade = 'C'
    elif score >=60:
        grade = 'D'
    else:
        grade = 'F'
    print(f"Score: {score}, Grade: {grade}")
score=85
calculate_grade(score)
score=100
calcualte_grade(score)
score=100
calculate_grade(score)
