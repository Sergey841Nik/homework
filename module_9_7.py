from math import sqrt

def is_prime(func):
    def wrapper(*args) -> int:
        res: int = func(*args)
        if res == 0:
            print("Нули дают только нули")
            return res
        end: int = int(sqrt(res)) + 1
        for div in range(2, end):
            if res % div == 0:
                print("Составное")
                return res
        print("Простое")
        return res
    return wrapper

@is_prime
def sum_three(*args) -> int:
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError("Необходимо передавать только целые числа")
    return sum(args)


print(sum_three(1, 2, 3))
print(sum_three(2, 3, 6))
print(sum_three(9, 0, 0))
print(sum_three(0, 0, 0))