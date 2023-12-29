class File:
    """
    Контекст менеджер File\n
    - теперь при попытке открыть несуществующий файл менеджер автоматически создаёт и открывает этот файл в режиме записи;\n
    - на выходе из менеджера подавляются все исключения,связанные с файлами.
    """

    def __init__(self, path: str, mode: str, encoding: str = 'utf8') -> None:
        self.filename = path
        self.mode = mode
        self.encoding = encoding

    # Не понимаю что здесь возвращает функция
    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


print('Задача 1. Работа с файлом 2')

with File('example.txt', 'w+') as file:
    file.write('Привет, человек\n')
    # file.write(12)
    file.write('Добрый день\n')
    file.write('Земля наша планета\n')

# ошибка не выдается, но если ставить ошибочное сообщение,
# то дальше программа ничего не делает
