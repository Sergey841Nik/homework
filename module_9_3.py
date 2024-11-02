class IncorrectLenList(Exception):
    pass


first: list[str] = ["Strings", "Student", "Computers"]
second: list[str] = ["Строка", "Урбан", "Компьютер"]

# проверка длины списков
if len(first) != len(second):
    raise IncorrectLenList("В данной задаче длина списков должна быть одинаковой")

# проверка типов
for str_ in first + second:
    if not isinstance(str_, str):
        raise TypeError("В данной задаче списки должны быть строками")

first_result = (len(i) - len(j) for i, j in zip(first, second) if len(i) != len(j))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(tuple(first_result))
print(tuple(second_result))
