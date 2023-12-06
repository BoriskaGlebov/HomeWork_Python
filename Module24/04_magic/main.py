print('Задача 04. Магия')


class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steem()
        elif isinstance(other, Earth):
            return Dirt()


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()


class Earth:
    def __str__(self):
        return 'Земля'


class Storm:
    def __str__(self):
        return f'Вода + Воздух = Шторм'


class Steem:
    def __str__(self):
        return f'Вода + Огонь = Пар'


class Dirt:
    def __str__(self):
        return f'Вода + Земля = Грязь'


class Lightning:
    def __str__(self):
        return f'Воздух + Огонь = Молния'


class Dust:
    def __str__(self):
        return f'Воздух + Земля = Пыль'


class Lava:
    def __str__(self):
        return f'Огонь + Земля = Лава'


water = Water()
air = Air()
fire = Fire()
earth = Earth()
print(water, air, fire, earth)
print(water + air)
print(water + fire)
print(water + earth)
print(air + fire)
print(air + earth)
print(fire + earth)
