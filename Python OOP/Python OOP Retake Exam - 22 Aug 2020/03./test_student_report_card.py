from project.student_report_card import StudentReportCard

# from testing.student_report_card import StudentReportCard

from unittest import TestCase


class StudentReportCardTests(TestCase):
    def setUp(self) -> None:
        self.student_report_card = StudentReportCard("Ani", 2)

    def test_init_if_proper_initialization(self):
        self.assertEqual("Ani", self.student_report_card.student_name)
        self.assertEqual(2, self.student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_student_name_if_empty_string_raise_error(self):
        with self.assertRaises(ValueError) as error:
            self.student_report_card.student_name = ''

        self.assertEqual("Student Name cannot be an empty string!", str(error.exception))

    def test_school_year_if_invalid_raise_error(self):
        with self.assertRaises(ValueError) as error:
            self.student_report_card.school_year = 0

        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.student_report_card.school_year = -1

        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.student_report_card.school_year = 13

        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

    def test_successful_year(self):
        self.student_report_card.school_year = 1
        self.assertEqual(1, self.student_report_card.school_year)

        self.student_report_card.school_year = 12
        self.assertEqual(12, self.student_report_card.school_year)

    def test_add_grade_in_grades_by_subject(self):
        self.student_report_card.add_grade("History", 4.0)
        self.assertEqual({"History": [4.0]}, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade("History", 6.0)
        self.assertEqual({"History": [4.0, 6.0]}, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade("Music", 6.0)
        self.assertEqual({"History": [4.0, 6.0], "Music": [6.0]}, self.student_report_card.grades_by_subject)

    def test_average_grade_by_subject_if_proper_result(self):
        self.student_report_card.add_grade("History", 4.0)
        self.student_report_card.add_grade("History", 6.0)

        self.assertEqual("History: 5.00", self.student_report_card.average_grade_by_subject())

        self.student_report_card.add_grade("Music", 6.0)
        self.assertEqual("History: 5.00\nMusic: 6.00", self.student_report_card.average_grade_by_subject())

    def test_average_grade_for_all_subjects_if_proper_result(self):
        self.student_report_card.add_grade("History", 4.0)
        self.student_report_card.add_grade("History", 6.0)
        self.student_report_card.add_grade("Music", 6.0)

        self.assertEqual("Average Grade: 5.33", self.student_report_card.average_grade_for_all_subjects())

        self.student_report_card.add_grade("Music", 4.0)
        self.assertEqual("Average Grade: 5.00", self.student_report_card.average_grade_for_all_subjects())

    def test_repr_if_represents_correct_info(self):
        self.student_report_card.add_grade("History", 4.0)
        self.student_report_card.add_grade("History", 6.0)
        self.student_report_card.add_grade("Music", 6.0)
        self.student_report_card.add_grade("Music", 4.0)

        result = "Name: Ani\n" \
                 "Year: 2\n" \
                 "----------\n" \
                 "History: 5.00\nMusic: 5.00\n" \
                 "----------\n" \
                 "Average Grade: 5.00"

        self.assertEqual(result, self.student_report_card.__repr__())
