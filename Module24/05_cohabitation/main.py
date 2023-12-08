from random import randint
from time import sleep


class Home:

    def __init__(self, fridge=50, safe_deposit=0):
        self.fridge = fridge
        self.safe_deposit = safe_deposit

    def __str__(self):
        return (f'Наполнение холодильника = {self.fridge}\n'
                f'Денег в сейфе = {self.safe_deposit}')


class Human:
    def __init__(self, name, home, satiety=50):
        self.name = name
        self.satiety = satiety
        self.home = home

    def __str__(self):
        return f'{self.name}: Сытость = {self.satiety}'

    def eat(self):
        self.satiety += 1
        self.home.fridge -= 1

    def work(self):
        self.satiety -= 1
        self.home.safe_deposit += 1

    def play(self):#Чуть накрутил, пусть хоть иногда умирают)
        self.satiety -= 2

    def shoping(self):#Чуть накрутил, пусть хоть иногда умирают)
        self.home.safe_deposit -= 2
        self.home.fridge += 1

    def life(self, cube):
        if self.satiety < 20 and self.home.fridge > 0:
            print(f'{self.name} покушал.')
            self.eat()
        elif self.home.fridge < 10 and self.home.safe_deposit >= 3:
            print(f'{self.name} сходил в магазин.')
            self.shoping()
        elif self.home.safe_deposit < 50:
            print(f'{self.name} сходил на работу')
            self.work()
        elif cube == 1:
            print(f'{self.name} сходил на работу')
            self.work()
        elif cube == 2:
            print(f'{self.name} целый день играл')
            self.eat()
        else:
            self.play()


print('Задача 05. Совместное проживание')

home_1 = Home()
print(home_1)
print()
with open('name.txt', 'r', encoding='utf_8') as name:
    humans = [Human(i_name.rstrip(), home_1) for i_name in name]
dead = False
for day in range(1, 365):
    # sleep(1)
    if dead:
        break
    print('-' * 80)
    print(f'Начался новый {day} день!')
    print(home_1)
    print()
    for human in humans:
        print(human)
        if human.satiety < 0:
            print(' Сосед помер')
            dead = True
            break
        cube = randint(1, 6)
        human.life(cube)
