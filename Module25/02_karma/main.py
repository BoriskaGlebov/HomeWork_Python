import logging

from random import randint


# TODO Я бы хотел понять как правильно пользоваться собственными исключениями?
#  Здесь это правильно или нет в соответствии с задачей?
#  Может лучше бы я создал под каждое название ошибки под класс от Exception?
#  Но тогда как их рандомно вызывать?#
#
class MyError(Exception):
    err_list = ['KillError',
                'DrunkError',
                'CarCrashError',
                'GluttonyError',
                'DepressionError', ]
    err_dict = {'KillError': 'Человека убил! Кармы не будет!',
                'DrunkError': 'Пил спиртное! Кармы не будет!',
                'CarCrashError': 'Машину разбил! Кармы не будет!',
                'GluttonyError': 'Опять объелся! Кармы не будет!',
                'DepressionError': 'Чего у тебя плохое настроение? '
                                   'Кармы не будет!'}

    def __str__(self):
        logging.basicConfig(level=logging.INFO, filename="karma.log", filemode="a",
                            format="%(asctime)s %(levelname)s %(message)s",encoding='utf8')
        rand_err_mess = randint(0, len(self.err_list) - 1)
        out_str = (f'{self.__class__.__name__} '
                   f'{self.err_list[rand_err_mess]} '
                   f'{self.err_dict[self.err_list[rand_err_mess]]}')
        logging.info(out_str)
        return out_str


class DzenProger:
    __carma = 500

    def __init__(self):
        self.sum_carma = 0

    def one_day(self):
        probability = randint(1, 10)
        try:
            if probability == 1:
                raise MyError
            else:
                self.sum_carma += randint(1, 7)
        except MyError:
            print(MyError())

    def get_carma_const(self):
        return self.__carma


print('Задача 02. Карма')
buddy = DzenProger()
while buddy.sum_carma <= buddy.get_carma_const():
    buddy.one_day()
    print(buddy.sum_carma)
