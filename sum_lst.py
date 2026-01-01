from typing import Iterable, Union


def sum_nested(values: Iterable[Union[int, list]]) -> int:
    """Рекурсивный подсчёт суммы элементов вложенных списков."""
    total = 0
    for item in values:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += int(item)
    return total



numbers = [1, [2, 3], [4, [5, 6]], [-1, -5], 0]

print("list =", numbers)
print("sum  =", sum_nested(numbers))
