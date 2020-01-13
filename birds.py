class Birds:

    def __init__(self, name, weight, vote, legs=2, wings=2):
        self.name = name
        self.weight = weight
        self.vote = vote
        self.legs = legs
        self.wings = wings

    hunger = 0
    food = 5

    def feed(self):
        if self.hunger < 51:
            self.hunger += self.food
            self.weight += 2
        else:
            print('Не кормить!')

    eggs = 0

    def pick_eggs(self):
        self.eggs += 2