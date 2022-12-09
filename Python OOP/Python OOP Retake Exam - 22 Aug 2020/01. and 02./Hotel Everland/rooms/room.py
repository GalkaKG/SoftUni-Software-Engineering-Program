from project.appliances.appliance import Appliance


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        
    @property
    def expenses(self):
        return self.__expenses
    
    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_expenses = 0
        for elements in args:
            for el in elements:
                if isinstance(el, Appliance):
                    total_expenses += el.get_monthly_expense()
                elif el.__class__.__name__ == "Child":
                    total_expenses += el.cost * 30
        self.expenses = total_expenses

