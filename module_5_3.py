class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors
        self.verif(number_of_floors)

    def verif(self, values: int):
        if not (
            isinstance(self.name, str)
            and isinstance(self.number_of_floors, int)
            and isinstance(values, (int, House))
        ):
            raise TypeError("Неверный фоомат(type) введённых данных")

    def __str__(self):
        return f"Название дома: {self.name}, количество этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors

    def __add__(self, other):
        self.verif(other)
        self.number_of_floors += other
        return self

    def __radd__(self, other):
        self.verif(other)
        return self.__add__(other)

    def __iadd__(self, other):
        self.verif(other)
        return self.__add__(other)

    def __eq__(self, other):
        self.verif(other)
        return self.number_of_floors == other

    # def __ne__(self, other):
    #     self.verif(other)
    #     return not self.__eq__(other) # Это помоему так и работает

    def __gt__(self, other):
        self.verif(other)
        return self.number_of_floors > other

    def __ge__(self, other):
        self.verif(other)
        return self.number_of_floors >= other

    def __lt__(self, other):
        self.verif(other)
        return self.number_of_floors < other

    def __le__(self, other):
        self.verif(other)
        return self.number_of_floors <= other

    def go_to(self, new_floor: int):
        self.verif(new_floor)
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")


hs1 = House("Горизонт", 15)
hs2 = House("Гуливер", 15)

print(hs1)
print(hs2)

print(hs1 == hs2)

hs1 = hs1 + 10
print(hs1)
print(hs1 == hs2)

hs2 += 5
print(hs2)

hs2 = 10 + hs2
print(hs2)

print(hs1 > hs2)
print(hs1 >= hs2)
print(hs1 < hs2)
print(hs1 <= hs2)
print(hs1 != hs2)
