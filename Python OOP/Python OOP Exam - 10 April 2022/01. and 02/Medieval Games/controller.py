class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def __find_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    @staticmethod
    def __check_if_player_cannot_duel(first_player, second_player):
        result = ''
        if first_player.stamina == 0:
            result += f"Player {first_player.name} does not have enough stamina." + "\n"
        if second_player.stamina == 0:
            result += f"Player {second_player.name} does not have enough stamina."
        return result.rstrip()

    def add_player(self, *players):
        players_added = []
        for player in players:
            if player not in self.players:
                players_added.append(player)
                self.players.append(player)
        return f"Successfully added: {', '.join(p.name for p in players_added)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player(player_name)

        if player.stamina == 100:
            return f"{player.name} have enough stamina."

        for supply in reversed(self.supplies):
            if type(supply).__name__ == sustenance_type:
                if player.stamina + supply.energy > 100:
                    player.stamina = 100
                else:
                    player.stamina += supply.energy
                self.supplies.remove(supply)
                return f"{player.name} sustained successfully with {supply.name}."

        if sustenance_type == "Food":
            raise Exception("There are no food supplies left!")
        if sustenance_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player(first_player_name)
        second_player = self.__find_player(second_player_name)

        result = self.__check_if_player_cannot_duel(first_player, second_player)
        if result:
            return result

        player_turn = first_player if first_player.stamina < second_player.stamina else second_player
        other_player = first_player if player_turn == second_player else second_player

        if other_player.stamina - (player_turn.stamina / 2) < 0:
            other_player.stamina = 0
        else:
            other_player.stamina -= (player_turn.stamina / 2)

        if player_turn.stamina - (other_player.stamina / 2) < 0:
            player_turn.stamina = 0
        else:
            player_turn.stamina -= (other_player.stamina / 2)

        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)
        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        output = ''
        for player in self.players:
            output += f"{player.__str__()}" + "\n"

        for supply in self.supplies:
            output += f"{supply.details()}" + "\n"

        return output.rstrip()
