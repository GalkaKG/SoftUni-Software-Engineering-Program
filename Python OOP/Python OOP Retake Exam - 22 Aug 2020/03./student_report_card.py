from typing import Dict, List


class StudentReportCard:
    def __init__(self, student_name: str, school_year: int):
        self.student_name = student_name
        self.school_year = school_year
        self.grades_by_subject: Dict[str, List[float]] = {}

    @property
    def student_name(self):
        return self.__student_name

    @student_name.setter
    def student_name(self, value):
        if value == '':
            raise ValueError("Student Name cannot be an empty string!")
        self.__student_name = value

    @property
    def school_year(self):
        return self.__school_year

    @school_year.setter
    def school_year(self, value):
        if not 1 <= value <= 12:
            raise ValueError("School Year must be between 1 and 12!")
        self.__school_year = value

    def add_grade(self, subject: str, grade: float):
        if subject not in self.grades_by_subject:
            self.grades_by_subject[subject] = []
        self.grades_by_subject[subject].append(grade)

    def average_grade_by_subject(self):
        report_for_each_subject = ''
        for subject, grades in self.grades_by_subject.items():
            average_grade = sum(grades) / len(grades)
            report_for_each_subject += f"{subject}: {average_grade:.2f}\n"
        return report_for_each_subject.strip()

    def average_grade_for_all_subjects(self):
        sum_all_grades = 0
        all_count = 0
        for grades in self.grades_by_subject.values():
            sum_all_grades += sum(grades)
            all_count += len(grades)
        return f"Average Grade: {sum_all_grades/ all_count :.2f}"

    def __repr__(self):
        report = f"Name: {self.student_name}\n" \
                 f"Year: {self.school_year}\n" \
                 f"----------\n" \
                 f"{self.average_grade_by_subject()}\n" \
                 f"----------\n" \
                 f"{self.average_grade_for_all_subjects()}"
        return report
