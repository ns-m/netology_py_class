from mammals import Mammals
from birds import Birds

goose_gray = Birds('Серый', 32, 'Кря-кря')
goose_white = Birds('Белый', 30, 'Кря-кря')
cow = Mammals('Манька', 350, 'Муу')
sheep_lamb = Mammals('Барашек', 150, 'Бее')
sheep_curly = Mammals('Кудрявый', 160, 'Бее')
chicken_koko = Birds('КоКо', 15, 'Ко-ко')
chicken_kukareku = Birds('Кука', 18, 'Ко-ко')
goat_horns = Mammals('Рога', 60, 'Мее')
goat_hooves = Mammals('Копыта', 50, 'Мее')
duck_mallard = Birds('Кряква', 20, 'Кряк-кряк')

class Animals4LegsMilk(Mammals):
    if cow:
        wool = 0
        milk = 250
        def feed(self):
            if self.hunger < 101:
                self.hunger += self.food
                self.milk += 5
            else:
                print('Не кормить!')

    if goat_horns or goat_hooves:
        wool = 50
        milk = 150
        def feed(self):
            if self.hunger < 81:
                self.hunger += self.food
                self.milk += 3
                self.wool += 4
            else:
                print('Не кормить!')

class Animals4LegsWool(Mammals):
    if sheep_lamb or goat_hooves:
        milk = 0
        def feed(self):
            if self.hunger < 91:
                self.hunger += self.food
                self.wool += 8
            else:
                print('Не кормить!')

print(cow.milk)
print(cow.weight)
cow.milky()
cow.feed()
print(cow.milk)
print(cow.weight)
print('---------------')
print(sheep_curly.wool)
print(sheep_curly.weight)
sheep_curly.cut()
sheep_curly.feed()
print(sheep_curly.wool)
print(sheep_curly.weight)
print('---------------')
animals = [goose_gray.__dict__, goose_white.__dict__, cow.__dict__, sheep_lamb.__dict__, sheep_curly.__dict__, chicken_koko.__dict__, chicken_kukareku.__dict__,
           goat_horns.__dict__, goat_hooves.__dict__, duck_mallard.__dict__]
animals_weight = 0
animals_weight_max = 0
for animal in animals:
    animals_weight += animal['weight']
    if animals_weight_max < animal['weight']:
        animals_weight_max = animal['weight']
    else:
        animals_weight_max = animals_weight_max
for animal in animals:
    for k, v in animal.items():
        if v == animals_weight_max:
            big_animal = animal['name']
print(f"Общий вес животных - {animals_weight} кг / Имя самого тяжелого животного - {big_animal}")

