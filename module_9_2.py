
first_strings: list[str] = ["Elon", "Musk", "Programmer", "Monitors", "Variable"]   
second_strings: list[str] = ["Task", "Git", "Comprehension", "Java", "Computer", "Assembler"]

#проверка на тип данных в списках перед началом работы
for str_ in first_strings + second_strings:
    if not isinstance(str_, str):
        raise TypeError(f"{str_} этот элемент не строка")

first_result: list[int] = [len(i) for i in first_strings if len(i) > 5]
second_result: list[tuple[int, int]] = [
    (i, j) for i in first_strings for j in second_strings if len(i) == len(j)
]
first_strings.extend(second_strings)
third_result: dict[str, int] = {i: len(i) for i in first_strings if len(i) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
