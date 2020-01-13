class Mammals:

    def __init__(self, name, weight, vote, legs=4, horns=2):
        self.name = name
        self.weight = weight
        self.vote = vote
        self.legs = legs
        self.horns = horns

    wool = 100

    def cut(self):
        if self.wool < 20:
            print('Хватит стричь!')
        else:
            self.wool -= 10

    milk = 100

    def milky(self):
        if self.milk < 10:
            print('Хватит доить!')
        else:
            self.milk -= 15

    hunger = 0
    food = 10

    def feed(self):
        if self.hunger < 101:
            self.hunger += self.food
            self.weight += 5
        else:
            print('Не кормить!')