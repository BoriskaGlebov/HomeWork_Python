class Property:
    def __init__(self, worth: float = 0):
        self.__worth = worth

    def get_worth(self):
        return self.__worth

    def tax(self, tax_rate):
        return round((self.get_worth() / tax_rate), 3)

    def __str__(self):
        return '{:,}'.format(self.get_worth())


class Apartament(Property):
    def tax(self, tax_rate=1000):
        return super().tax(tax_rate)


class Car(Property):
    def tax(self, tax_rate=200):
        return super().tax(tax_rate)


class CountryHouse(Property):
    def tax(self, tax_rate=500):
        return super().tax(tax_rate)


print('Задача 01. Налоги')

print('Добро пожаловать в Налоговую!')
tot_money = float(input('Сколько у вас денег? '))
prop_list = [Apartament(float(input('Введите стоимость жилья? '))),
             Car(float(input('Введите стоимость машины? '))),
             CountryHouse(float(input('Введите стоимость загородного дома')))]
tot_tax = 0
for el in prop_list:
    tot_tax += el.tax()
if tot_tax <= tot_money:
    print(f'Вы можете оплатить все налоги = {tot_tax}')
else:
    print(f'Вам не хватает денег для оплаты налога {tot_money - tot_tax}')
