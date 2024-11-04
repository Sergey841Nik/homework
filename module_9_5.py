class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start: int, stop: int, step: int = 1):
        self.__valid_value(start, stop, step)  # проверка на корректность шага
        self.__start = start
        self.__stop = stop
        self.__step = step
        self.__pointer = start

    def __valid_value(self, start, stop, step):
        if step == 0:
            raise StepValueError("Шаг не может быть равен 0")
        elif start > stop and step > 0:
            raise StepValueError("Начальное значение больше конечного")
        elif start < stop and step < 0:
            raise StepValueError("Начальное значение меньше конечного")

    def __iter__(self):
        self.__pointer = self.__start
        return self

    def __next__(self):
        if self.__step > 0:
            if self.__pointer <= self.__stop:
                result = self.__pointer
                self.__pointer += self.__step
                return result
            else:
                raise StopIteration
        elif self.__step < 0:
            if self.__pointer >= self.__stop:
                result = self.__pointer
                self.__pointer += self.__step
                return result
            else:
                raise StopIteration


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=" ")
except StepValueError as e:
    print(e)

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)

for i in iter2:
    print(i, end=" ")
print()

for i in iter3:
    print(i, end=" ")
print()

for i in iter4:
    print(i, end=" ")
print()

try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=" ")
    print()
except StepValueError as e:
    print(e)
