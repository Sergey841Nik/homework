
#функция вычисляет сумму квадратов всех элементов списка
def max_sum_squares(lst: list[int | float]) -> int | float:
    return sum(map(lambda x: x ** 2, lst))


def apply_all_func(int_list: list[int | float], *functions) -> dict:
    results: dict ={}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


print(apply_all_func([1, 2, 3, 4], max_sum_squares, max, sum))
print(apply_all_func([1, 2, 3, 4], len, sorted))