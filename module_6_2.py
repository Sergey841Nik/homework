class Vehicle:
    __COLOR_VARIANTS: list[str] = ["red", "green", "blue"]

    def __init__(self, owner: str, model, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power} л.с."

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(
            self.get_model(),
            self.get_horsepower(),
            self.get_color(),
            f"Владелец: {self.owner}",
            sep="\n",
        )

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT: int = 5

    def get_limit_passengers(self):
        return f"В траспортное средство гражданина {self.owner} можно усадить до {self.__PASSENGERS_LIMIT} человек"

    # Переопределяем метод
    # чтобы не потерять выводимую информацию из базового класса
    def print_info(self):
        # Vehicle.print_info(self) #вызовем метод из базового класса Vehicle и передадим туда экземпляр класс, который уже содержит всю информацию
        super().print_info()  # но лучше так, чтобы не зависить от имени класса
        print(self.get_limit_passengers())


def main():
    vl = Sedan("Игорь", "Opel", 112, "red")
    vl.print_info()
    print("-" * 50)
    # Игорь продал свою машину Василию
    vl.owner = "Василий"
    vl.print_info()
    print("-" * 50)
    # Василий поменял цвет машины на зелёный
    vl.set_color("Grenn")
    vl.print_info()
    print("-" * 50)
    # Василий подумал и решил поменять на синий
    vl.set_color("BluE")
    # Василий обратился к гаражному слесарю Коле и тот форсиорвал ему двигатель, что строго запрещено документацией
    vl.__dict__["_Vehicle__engine_power"] = 200
    vl.print_info()


if __name__ == "__main__":
    main()
