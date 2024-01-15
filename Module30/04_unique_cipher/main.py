from collections import Counter
from functools import reduce


def count_unique_characters(text: str) -> int:
    """Ищит количество уникальных символов в тексте"""
    # text_filtered = dict(filter(lambda el: el[1] == 1, Counter(text.lower()).items()))
    result = reduce(lambda a, b: a + b, dict(filter(lambda el: el[1] == 1, Counter(text.lower()).items())).values())
    return result


print('Задача 4. Уникальный шифр')

# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
