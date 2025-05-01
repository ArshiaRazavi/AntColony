import environment, ant

env = environment.Environment(width=200, height=100)
env.place_food_randomly(count=5)

ants = []
for i in range(10):
    ants.append(ant.Ant(x=0, y=0))

