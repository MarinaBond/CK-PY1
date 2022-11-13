import random
from random import randint


def get_unique_list_numbers(a=-10, b=10, c=15) -> list[int]:
    list_ = []
    while len(list_) <c:
        x = randint(a, b)
        if x not in list_:
            list_.append(x)

    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
