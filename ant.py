class ant ():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.carrying_food = False

    def move(self, x, y):
        # Look at neighboring cells and update self.x and self.y
        
        pass
    
    def update(self):
        # Decide whether to pick up food or drop pheromone
        pass

    def __str__(self):
        return f"Ant(name={self.name}, age={self.age}, color={self.color})"

    def __repr__(self):
        return f"Ant(name={self.name}, age={self.age}, color={self.color})"