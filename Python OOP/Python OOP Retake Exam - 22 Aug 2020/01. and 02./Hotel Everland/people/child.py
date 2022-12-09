class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.food_cost = food_cost  # money for a day

        self.cost = 0
        for toy in toys_cost:
            self.cost += toy
        self.cost += food_cost
        
