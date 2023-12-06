print('Задача 3. Отцы, матери и дети')


class Parent:
    def __init__(self, name, age, *childrens):
        self.name = name
        self.age = age
        self.children_list = list(*childrens)

    def create_children(self, name, age, calm=False, satisfied=False):
        if self.age - age < 16:
            print('Возраст ребенка должен быть на 16 меньше родителя')
            age = self.age - 16
        children_new = Children(name, age, calm, satisfied)


    def feed_children(self):
        for children in self.children_list:
            if children.calm == 'Голоден':
                children.calm = children.calm_dict[False]
                print('Накормила деточку!')
            else:
                print('Деточка не голоден!')

    def calm_children(self):
        for children in self.children_list:
            if children.satisfied == 'Нервничает':
                children.satisfied = children.satisfied_dict[True]
                print('Успокоил деточку!')
            else:
                print('Деточка спокоен!')


class Children:
    calm_dict = {True: 'Голоден', False: 'Не голоден'}
    satisfied_dict = {True: 'Спокоен', False: 'Нервничает'}

    def __init__(self, name, age, calm=False, satisfied=True):
        self.name = name
        self.age = age
        self.calm = self.calm_dict[calm]
        self.satisfied = self.satisfied_dict[satisfied]

    def children_info(self):
        print(f'{self.name} возрастом {self.age}. {self.calm}, {self.satisfied}')

#Создал экземпляр мать без детей
mother = Parent('Света', 36)
print('\nмать', mother.children_list)
#Создаю три ребенка,у  ондого слишком большой возраст и его возраст поправится на -16 от возраста матери
mother.create_children('Вася', 30, True, False)
mother.create_children('Артурчик', 10, False, True)
mother.create_children('Мишутка', 15)
print('\nмать', mother.children_list)
#Проверяю детишек
for children in mother.children_list:
    children.children_info()
# Создал отцы с детьми матери
father = Parent('Бориска', 32, mother.children_list)
print('\nпапа', father.children_list)
#Проверяю детишек
for children in father.children_list:
    children.children_info()
print()
#отец накормил детей, а мать успокоила и проверил их состояния после
father.feed_children()
mother.calm_children()
for children in mother.children_list:
    children.children_info()
for children in father.children_list:
    children.children_info()
