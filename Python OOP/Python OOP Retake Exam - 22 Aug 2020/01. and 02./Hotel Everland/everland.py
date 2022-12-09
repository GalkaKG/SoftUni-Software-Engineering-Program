from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost

        return f"Monthly consumptions: {total_consumption:.2f}$."

    def pay(self):
        result = ''
        for room in self.rooms:
            if room.budget >= room.expenses:
                room.budget -= room.expenses + room.room_cost
                result += f"{room.family_name} paid {(room.expenses + room.room_cost):.2f}$ and have" \
                          f" {room.budget:.2f}$ left.\n"
            else:
                self.rooms.remove(room)
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
        return result.strip()

    def status(self):
        all_people_in_the_hotel = sum([room.members_count for room in self.rooms])
        result = f'Total population: {all_people_in_the_hotel}\n'

        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$," \
                      f" Expenses: {room.expenses:.2f}$\n"
            if room.__class__.__name__ == "YoungCoupleWithChildren":
                child_number = 1
                for child in room.children:
                    result += f"--- Child {child_number} monthly cost: {(child.cost * 30):.2f}$\n"
                    child_number += 1

            if room.__class__.__name__ != "AloneOld":
                total_expenses = 0
                for appliance in room.appliances:
                    total_expenses += appliance.get_monthly_expense()

                result += f"--- Appliances monthly cost: {total_expenses:.2f}$\n"

        return result.strip()
