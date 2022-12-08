from project.controller import Controller


aquarium1 = Controller()
print(aquarium1.add_aquarium("SaltwaterAquarium", "Lili's"))
print(aquarium1.add_aquarium("Pacific", "Suzy's"))
print(aquarium1.add_decoration("Plant"))
print(aquarium1.add_decoration("Ornament"))
print(aquarium1.add_decoration("Toy"))
print(aquarium1.add_fish("Lili's", "SaltwaterFish", "Nemo", "asd", 50))

aquarium2 = Controller()
print(aquarium2.add_aquarium("FreshwaterAquarium", "Bobi's"))
aquarium3 = Controller()
print(aquarium2.add_fish("Bobi's", "FreshwaterFish", "Gupi", "h45", 80))
aquarium_extra = Controller()
print(aquarium_extra.add_aquarium("SaltwaterAquarium", "Extra"))
print(aquarium_extra.add_fish("Extra", "SaltwaterFish", "Gogo", "kr", 80))
print(aquarium_extra.feed_fish("Extra"))
print(aquarium_extra.calculate_value("Extra"))
print(aquarium_extra.add_decoration("Plant"))
print(aquarium_extra.insert_decoration("Extra", "Plant"))
print(aquarium_extra.add_fish("Extra", "SaltwaterFish", "Shark", "hlm", 150 ))
print(aquarium_extra.report())
