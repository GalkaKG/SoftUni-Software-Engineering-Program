from project.team import Team
from unittest import TestCase


class TeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team("Team")

    def test_init_is_proper_initialization(self):
        self.assertEqual("Team", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_if_invalid_raise_error(self):
        with self.assertRaises(ValueError) as error:
            self.team.name = "Team1"

        self.assertEqual("Team Name can contain only letters!", str(error.exception))

    def test_add_member_if_name_not_exist_add_it_in_members(self):
        result = self.team.add_member(Ivan=20, Gosho=15)
        self.assertEqual(f"Successfully added: Ivan, Gosho", result)

        result = self.team.add_member(Ivan=18, Gosho=13)
        self.assertEqual(f"Successfully added: ", result)

    def test_remove_member_name_not_exist(self):
        result = self.team.remove_member("Gosho")
        self.assertEqual(f"Member with name Gosho does not exist", result)

    def test_remove_member_successfully_removed(self):
        self.team.add_member(Ivan=18, Gosho=15)
        result = self.team.remove_member("Gosho")

        self.assertEqual(f"Member Gosho removed", result)
        self.assertEqual({"Ivan": 18}, self.team.members)

    def test_gt_if_return_true(self):
        other = Team("Other")
        other.members = {"Lili": 28}
        self.team.members = {"Ivan": 18, "Gosho": 15}

        self.assertEqual(True, self.team.__gt__(other))

    def test_gt_if_return_false(self):
        other = Team("Other")
        other.members = {"Lili": 28, "Gosho": 15}
        self.team.members = {"Ivan": 18}

        self.assertEqual(False, self.team.__gt__(other))

    def test_len_return_len_members(self):
        self.team.members = {"Lili": 28, "Gosho": 15}
        self.assertEqual(2, self.team.__len__())

    def test_add_concatenate_is_proper(self):
        other = Team("Other")
        self.team.members = {"Ivan": 18}
        other.members = {"Gosho": 15}
        new_team = self.team.__add__(other)

        self.assertEqual("TeamOther", new_team.name)
        self.assertEqual({"Ivan": 18, "Gosho": 15}, new_team.members)

    def test_str_proper_represent_with_members(self):
        self.team.members = {"Ivan": 18, "Gosho": 15, "Maria": 15}
        result = f"Team name: Team\nMember: Ivan - 18-years old\nMember: Gosho - 15-years old\n" \
                 f"Member: Maria - 15-years old"
        self.assertEqual(result, self.team.__str__())
