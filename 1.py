class Animal:
    amount_of_limbs = 4

class Mammals(Animal):
    first_food = 'milk'
class predators(Animal):
    food = 'meat'
    def _kill(self):
        print('Predator got some food')

class carnivores(Animal):
    food = 'plant'
    def _passture(self):
        print('Carnivore went to eat some plants')

class Lion(predators):
    size = 'big'
    color = 'yellow'
    def __init__(self):
        print(self.size)
        print(self.color)
        print(self.food)

class Horse(carnivores):
    size = 'big'
    color = 'lots of colours'
    def __init__(self):
        print(self.size)
        print(self.color)
        print(self.food)


Lion = Lion()
Lion._kill()
Horse = Horse()
Horse._passture()