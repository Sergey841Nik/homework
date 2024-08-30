first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")


def proverka_ravenstva(n1, n2, n3):
    try:
        n1, n2, n3 = int(n1), int(n2), int(n3)
        if n1 * n2 * n3 == n1**3:
            return 3
        elif n1 == n2 or n1 == n3 or n2 == n3:
            return 2
        else:
            return 0
    except ValueError:
        print("Вы ввели не целое число, а так нельзя мы такого не любим")


print(proverka_ravenstva(first, second, third))
