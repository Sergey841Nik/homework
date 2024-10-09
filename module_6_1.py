
class Animal:
    name: str
    mass: int
    alive: bool = True
    fed: bool = False

    def __init__(self, name: str, mass: int) -> None:
        self.name = name
        self.mass = mass

    def validate(self):
        if not (
            isinstance(self.name, str)
            and isinstance(self.mass, int)
            and isinstance((self.alive, self.fed), bool)
        ):
            raise TypeError("Нерный тип данных")

    def __gt__(self, other):
        return self.mass > other

    def __lt__(self, other):
        return self.mass < other


class Plant:
    name: str
    edible: bool = False

    def __init__(self, name: str):
        self.name = name

    def validate(self):
        if not (isinstance(self.name, str) and isinstance(self.edible, bool)):
            raise TypeError("Нерный тип данных")


class Predator(Animal):
    #Дополнил класс сверх ДЗ. Мне кажется несправедливо хищнику питаться только растениями
    def eat(self, food):
        if self.fed:
            return f"{self.name} сыт и проходит мимо {food.name}"
        else:
            if isinstance(food, Animal):
                if self > food:
                    self.fed = True
                    food.alive = False
                    return f"{self.name} съел {food.name}"
                else:
                    return f"{food.name} напугал {self.name}"

            elif isinstance(food, Plant):
                if food.edible:
                    self.fed = True
                    return f"{self.name} съел {food.name}"
                elif not food.edible:
                    self.alive = False
                    return f"{self.name} съел {food.name} отравился и умер"


class Herbivores(Animal):

    def eat(self, food):
        if self.fed:
            return f"{self.name} сыт и проходит мимо {food.name}"
        else:
            if not (self.fed and food.edible):
                self.fed = True
                return f"{self.name} съел {food.name}"
            elif food.edible:
                self.alive = False
                return f"{self.name} съел {food.name} отравился и умер"


class Flower(Plant):
    pass


class Fruit(Plant):
    edible: bool = True


def main():
    # Создадим сущности и выведем результат их взаимодействия
    pr = Predator(name="Волк", mass=90)
    mn = Herbivores("Заяц", 5)
    print(pr.eat(mn))
    pr1 = Predator(name="Медведь", mass=300)
    mn1 = Herbivores("Слон", 3000)
    print(pr1.eat(mn1))
    fl = Flower("Какя-то краная ягода")
    print(pr.eat(fl))
    print(pr1.eat(fl))
    fr = Fruit("Яблоко")
    print(mn1.eat(fr))


if __name__ == "__main__":
    main()
