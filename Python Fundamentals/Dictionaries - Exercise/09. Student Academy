rows = int(input())
final_dict = {}

for i in range(rows):
    student_name = input()
    grade = float(input())
    if student_name not in final_dict:
        final_dict[student_name] = []

    final_dict[student_name].append(grade)

for student, grade in final_dict.items():
    sum_grades = 0
    for gr in grade:
        sum_grades += gr
    avg_grade = sum_grades / len(grade)
    if avg_grade >= 4.50:
        print(f'{student} -> {avg_grade:.2f}')
