
def personal_sum(numbers) -> tuple:
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {number}")
    return result, incorrect_data

def calculate_average(numbers):
    try:
        tupl_ = personal_sum(numbers)
        return tupl_[0] / (len(numbers) - tupl_[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None
    

print(calculate_average("1, 2, 3"))
print(calculate_average([1, 2, 3, "Десять"]))
print(calculate_average([1, "Строка", 3, "Ещё Строка"]))
print(calculate_average(567))
print(calculate_average([42, 15, 36, 13]))
