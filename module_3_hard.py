data_structure = [
    [1, 2, 3],
    {"a": 4, "b": 5},
    (6, {"cube": 7, "drum": 8}),
    "Hello",
    ((), [{(2, "Urban", ("Urban2", 35))}]),
]


def calculate_structure_sum(date):
    total_sum = 0

    def recurse(item):
        nonlocal total_sum
        if isinstance(item, (list, tuple, set)):
            for element in item:
                recurse(element)
        elif isinstance(item, dict):
            for key, value in item.items():
                recurse(key)
                recurse(value)
        else:
            if isinstance(item, int):
                # print(item)
                total_sum += item
            if isinstance(item, str):
                # print(item)
                total_sum += len(str(item))

    recurse(date)

    return total_sum


print(calculate_structure_sum(data_structure))
