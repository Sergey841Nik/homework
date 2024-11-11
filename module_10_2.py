from threading import Thread
from time import sleep

class PowerKnightError(Exception):
    pass

class Knight(Thread):
    def __init__(self, name: str, power: int) -> None:
       self.__isvalid(name, power)  # проверка на корректность переданных данных
       super().__init__(name=name)
       self.name: str = name
       self.power: int = power
       self.__enemy: int = 100

    def  __isvalid(self, name, power) -> None:
        if not isinstance(name, str) or not isinstance(power, int):
            raise TypeError("Неверный тип переданных данных")
        if power > 100:
            raise PowerKnightError("Не бывает таких сильных рыцарей")
        elif power <= 0:
            raise PowerKnightError("С такой силой это и не рыцарь вообще")
        
    def run(self) -> None:  # запуск потока
        print(f"{self.name}, на нас напали!")
        self.__battle_knight(self.__enemy, self.power)


    def __battle_knight(self, enemy: int, power: int) -> None: # битва
        number_days_battle = divmod(enemy, power) #определяем количество дней битвы с возможным остатком

        for day in range(1, number_days_battle[0]+1):
            sleep(1)
            enemy -= power
            print(f"{self.name} сражается {day}..., осталось {enemy} вражеских воинов.")

        if number_days_battle[1]: #проверяем есть ли остаток от деления
            time_victory_over_remnants_enemies = round(number_days_battle[1] / power * 24) #время для победы над остатками врагов
            sleep(number_days_battle[1] / power)
            print(f"{self.name} одолел остатки врагов за {time_victory_over_remnants_enemies} часа(часов, час)")
            print(f"{self.name} одержал победу спустя {day} дней(дня) и {time_victory_over_remnants_enemies} часа(часов, час)!")
        else:
            print(f"{self.name} одержал победу спустя {day} дней(дня)")


kn1 = Knight("СирИван", 10)
kn2 = Knight("СирПетр", 30)

kn1.start()
kn2.start()
kn1.join()
kn2.join()
