import random
from monsters import Monster, MonsterBerserk


class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ",
              round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
    # Целитель:
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)

    def __init__(self, name):
        super().__init__(name)
        self.set_power(self.get_power() * 3)

    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # исцеление) на выбранную им цель

    def attack(self, target: Monster):
        print(f'{self.name} атакует {target.name}')
        self.damage = self.get_power() / 2

        target.take_damage(self.damage)

    def take_damage(self, damage):
        rez_damage = damage * 1.2
        self.set_hp(self.get_hp() - rez_damage)
        super().take_damage(rez_damage)

    def healing(self, target: Hero):
        print(f'{self.name} полечил {target.name} + {round(self.get_power())} ')
        target.set_hp(target.get_hp() + self.get_power())

    def make_a_move(self, friends: list, enemies: list):
        super().make_a_move(friends, enemies)
        min_health = min([hero.get_hp() for hero in friends])
        for hero in friends:
            if hero.get_hp() == min_health and hero.get_hp() < 100:
                print(f'{self.name} лечу того кому нужнее!')
                self.healing(hero)
                break
        else:
            max_pover = max([monster.get_power() for monster in enemies])
            target = 0
            for monster in enemies:
                if max_pover == monster.get_power():
                    target = monster

            # target = random.choice(enemies)
            self.attack(target)
        print()

    def __str__(self):
        return 'Name: {0:<18}|\tHP: {1:.2f}'.format(self.name, self.get_hp())


class Tank(Hero):

    # Танк:
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    def __init__(self, name, defense=1):
        super().__init__(name)
        self.defense = defense
        self.shield = False

    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # поднять щит/опустить щит) на выбранную им цель

    def shield_up(self):
        if self.shield:
            print(f'{self.name} опустил щит ')
            self.shield = False
            self.defense /= 2
            self.set_power(self.get_power() * 2)
        else:
            print(f'{self.name} поднял щит ')
            self.shield = True
            self.defense *= 2
            self.set_power(self.get_power() / 2)

    def attack(self, target: Monster):
        print(f'{self.name} атакует {target.name}')
        damage = self.get_power() / 2
        target.take_damage(damage)

    def take_damage(self, damage):
        rez_damage = damage / self.defense
        self.set_hp(self.get_hp() - rez_damage)
        super().take_damage(rez_damage)

    def make_a_move(self, friends: list, enemies: list):
        super().make_a_move(friends, enemies)
        if self.get_hp() < 100 and not self.shield:
            self.shield_up()
        # print('Атакую случайного врага')
        target = random.choice(enemies)
        self.attack(target)
        print()

    def __str__(self):
        return 'Name: {0:<18}|\tHP: {1:.2f}'.format(self.name, self.get_hp())


class Attacker(Hero):
    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 1

    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down.
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)
    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель
    def power_up(self):
        print(f'{self.name} Усилился. Наносимый урон увеличился в два раза, получаемый урон уменьшился в два раза!')
        self.power_multiply *= 2

    def power_down(self):
        print(f'{self.name} Ослабился. Наносимый урон уменьшился в два раза, получаемы урон увеличился в два раза!')
        self.power_multiply /= 2

    def attack(self, target: Monster):
        print(f'{self.name} атакует {target.name}')
        damage = self.get_power() * self.power_multiply
        target.take_damage(damage)
        if self.power_multiply > 1:
            self.power_down()

    def take_damage(self, damage):
        rez_damage = damage * self.power_multiply
        self.set_hp(self.get_hp() - rez_damage)
        super().take_damage(rez_damage)

    def make_a_move(self, friends: list, enemies: list):
        super().make_a_move(friends, enemies)
        target = random.choice(enemies)
        for monsters in enemies:
            if isinstance(monsters, MonsterBerserk):
                target = monsters
        if self.power_multiply <= 1:
            self.power_up()
        else:
            self.attack(target)
        print()

    def __str__(self):
        return 'Name: {0:<18}|\tHP: {1:.2f}'.format(self.name, self.get_hp())
