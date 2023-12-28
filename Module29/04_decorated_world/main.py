# @decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs): # отсюда уже сами!
    pass

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


print('Задача 4. Весь мир — декоратор…')

decorated_function("Юзер", 101)
