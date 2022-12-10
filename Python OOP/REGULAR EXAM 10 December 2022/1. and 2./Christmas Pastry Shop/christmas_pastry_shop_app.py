from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def __find_booth_for_reservation(self, number_of_people):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                return booth

    def __find_booth(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth

    def __find_delicacy(self, delicacy_name):
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                return delicacy

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in [d.name for d in self.delicacies]:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ["Gingerbread", "Stolen"]:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if type_delicacy == "Gingerbread":
            self.delicacies.append(Gingerbread(name, price))
        elif type_delicacy == "Stolen":
            self.delicacies.append(Stolen(name, price))

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ["Open Booth", "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")

        if type_booth == "Open Booth":
            self.booths.append(OpenBooth(booth_number, capacity))
        elif type_booth == "Private Booth":
            self.booths.append(PrivateBooth(booth_number, capacity))

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = self.__find_booth_for_reservation(number_of_people)

        if booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth(booth_number)
        delicacy = self.__find_delicacy(delicacy_name)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.__find_booth(booth_number)
        bill = 0

        bill += booth.price_for_reservation
        for delicacy in booth.delicacy_orders:
            bill += delicacy.price
        self.income += bill

        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
