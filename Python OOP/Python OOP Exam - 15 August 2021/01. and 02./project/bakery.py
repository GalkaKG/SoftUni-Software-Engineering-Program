from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def _find_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def add_food(self, food_type: str, name: str, price: float):
        if name in [f.name for f in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == "Bread":
            self.food_menu.append(Bread(name, price))
        elif food_type == "Cake":
            self.food_menu.append(Cake(name, price))

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if name in [d.name for d in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type == 'Tea':
            self.drinks_menu.append(Tea(name, portion, brand))
        elif drink_type == 'Water':
            self.drinks_menu.append(Water(name, portion, brand))

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_number in [t.table_number for t in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type == "InsideTable":
            self.tables_repository.append(InsideTable(table_number, capacity))
        elif table_type == "OutsideTable":
            self.tables_repository.append(OutsideTable(table_number, capacity))

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        food_that_is_not_in_the_menu = []
        table = self._find_table(table_number)
        if not table:
            return f"Could not find table {table_number}"

        for food_name in food_names:
            for food in self.food_menu:
                if food_name == food.name:
                    table.order_food(food)
            if food_name not in [f.name for f in self.food_menu]:
                food_that_is_not_in_the_menu.append(food_name)

        result = f'Table {table_number} ordered:' + '\n'
        for food_name in table.food_orders:
            result += repr(food_name) + '\n'

        result += f"{self.name} does not have in the menu:" + "\n"
        for food_name in food_that_is_not_in_the_menu:
            result += food_name + "\n"

        return result.strip()

    def order_drink(self, table_number: int, *drinks_names):
        table = self._find_table(table_number)
        if not table:
            return f"Could not find table {table_number}"

        drinks_not_in_the_menu = []

        for drink_name in drinks_names:
            for drink_in_menu in self.drinks_menu:
                if drink_name == drink_in_menu.name:
                    table.order_drink(drink_in_menu)
            if drink_name not in [d.name for d in self.drinks_menu]:
                drinks_not_in_the_menu.append(drink_name)

        result = f"Table {table_number} ordered:" + "\n"
        for drink in table.drink_orders:
            result += repr(drink) + '\n'

        result += f"{self.name} does not have in the menu:" + "\n"
        for drink_name in drinks_not_in_the_menu:
            result += drink_name + '\n'

        return result.strip()

    def leave_table(self, table_number: int):
        table = self._find_table(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            result += table.free_table_info() + "\n"

        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
