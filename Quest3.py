#The Wizard Grades
grade_dict={
    (80,100):'A',
    (70,79): 'B',
    (60,69): 'C',
    (50,59): 'D',
    (0,49): 'F'
}
def calculate_grade(mark):
    for grade_range, ranking in grade_dict.items():
        if grade_range[0]<=mark<=grade_range[1]:
            return ranking
        else:
            return 'Invalid score'
calculate_grade(40)            