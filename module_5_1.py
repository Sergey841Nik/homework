
class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor+1):
                print(floor)
        else:
            print("Такого этажа не существует")


hs1 = House("ЖК Горизонт", 16)
hs2 = House("ЖК Барак", 2)

hs1.go_to(7)
hs2.go_to(0)
