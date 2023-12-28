class Data:
    """
    Класс Date, который должен:\n
    - проверять числа даты на корректность;
    - конвертировать строку даты в объект класса Date, состоящий из соответствующих числовых значений дня, месяца и года.
    """

    @classmethod
    def from_string(cls, data_string: str) -> str:
        """Превращает дату в нужный формат"""
        data_list = data_string.split('-')
        out_str = 'День: {:<10} Месяц: {:<10} Год: {:<10}'.format(*data_list)
        return out_str

    @classmethod
    def is_date_valid(cls, data_string: str) -> bool:
        """Проверяет дату на правильность"""
        data_list: list[str] = data_string.split('-')
        if len(data_list) == 3:
            for num, el in enumerate(data_list):
                if not el.isdigit():
                    return False
                elif num == 0 and not (0 < int(el) < 30):
                    return False
                elif num == 1 and not (0 < int(el) < 13):
                    return False
            else:
                return True
        else:
            return False


pass

print('Задача 3. Дата')
data = Data.from_string('10-12-2077')
print(data)
print(Data.is_date_valid('10-12-2077'))
print(Data.is_date_valid('40-12-2077'))

