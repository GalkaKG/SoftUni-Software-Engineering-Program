from typing import Dict


class Team:
    def __init__(self, name: str):
        self.name = name
        self.members: Dict[str, int] = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise ValueError("Team Name can contain only letters!")
        self.__name = value

    def add_member(self, **name_age):
        added_members_by_name = []
        for name, age in name_age.items():
            if name not in self.members:
                self.members[name] = age
                added_members_by_name.append(name)
        return f"Successfully added: {', '.join(added_members_by_name)}"

    def remove_member(self, name: str):
        if name in self.members:
            del self.members[name]
            return f"Member {name} removed"
        else:
            return f"Member with name {name} does not exist"

    def __gt__(self, other):  # "other" is another instance of class Team!
        if len(self.members) > len(other.members):
            return True
        return False

    def __len__(self):
        return len(self.members)

    def __add__(self, other):  # "other" is another instance of class Team!
        new_team_name = f"{self.name}{other.name}"
        new_team = Team(new_team_name)
        new_team.add_member(**self.members)
        new_team.add_member(**other.members)
        return new_team

    def __str__(self):
        result = [f"Team name: {self.name}"]
        members = list(sorted(self.members.items(), key=lambda x: (-x[1], x[0])))
        result.extend([f"Member: {x[0]} - {x[1]}-years old" for x in members])
        return "\n".join(result)
