import numpy as np

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pheromones = np.zeros((width, height))
        self.food = np.zeros((width, height), dtype=bool)
        self.nest = (width // 2, height // 2)

    def evaporate_pheromones(self, rate=0.01):
        self.pheromones *= (1 - rate)

    def place_food_randomly(self, count=5):
        # Place food in random cells
        pass
