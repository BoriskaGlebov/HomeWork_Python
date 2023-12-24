from collections import defaultdict


class Steak:
    steak_dict = defaultdict(list)

    def new_task(self, task: str, priority: int = 0):
        Steak.steak_dict[priority].append(task)

    def pop_task(self, task: str):
        for key, value in Steak.steak_dict.items():
            for num, elem in enumerate(value):
                if elem == task:
                    Steak.steak_dict[key].remove(elem)
                    return 1
        else:
            print('Такой задачи нет!')
            return 0


class TaskManager:
    el = Steak()

    def new_task(self, task: str, priority: int):
        TaskManager.el.new_task(task, priority)

    def del_task(self, task):
        TaskManager.el.pop_task(task)

    def __str__(self):
        for k, v in sorted(TaskManager.el.steak_dict.items()):
            print(k, end=' ')
            for el in v:
                print(el + ';', end=' ')
            print('')
        return ''


print('Задача 05. Стек')
manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.del_task('сдать дз')
print(manager)
manager.del_task('сдать дз')
