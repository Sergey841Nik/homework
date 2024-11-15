from queue import Queue
from collections import deque
from threading import Thread
from time import sleep
from random import randint

#класс для проверки корректности переданных данных
class Valid:
    def valid(self, values, types_) -> None:
        if not isinstance(values, types_):
            raise TypeError(f"В {self} передан не верный тип данных")
        
    def valid_iter(self, iter_, types_) -> None:
        for value in iter_:
            self.valid(value, types_)


class Table(Valid):
    def __init__(self, number: int) -> None:
        self.valid(number, int)
        self.number: int = number
        self.guest = None

class Guest(Thread, Valid):
    def __init__(self, name: str) -> None:
        self.valid(name, str)
        super().__init__(name=name)
    
    def run(self) -> None:
        duration_of_eating: int = randint(3, 10)
        sleep(duration_of_eating)


class Cafe(Valid):
    def __init__(self, table: list[Table] | tuple[Table]) -> None:
        self.valid(table, (list, tuple))
        self.valid_iter(table, Table)
        self.table: list[Table] = table
        self.queur = Queue()

    def guest_arrival(self, guests: list[Guest] | tuple[Guest]) -> None:
        self.valid_iter(guests, Guest)
        guests: deque = deque(guests) #создаётся объект двухсторонней очереди 
        for table in self.table:
            if not table.guest and guests:
                guest: Guest = guests.popleft() #достаём элемент из очереди слева (первый туда положенный)
                table.guest = guest
                print(f"{guest.name} сел(-а) за стол номер {table.number}")
                guest.start()

        if guests:
            for guest in guests: #если бы не это условии то не надо было бы создавать deque обошлись бы Queue
                self.queur.put(guest)
                print(f"{guest.name} в очереди")
    
    def discuss_guests(self) -> None:
        while not self.queur.empty() or any(table.guest is not None for table in self.table):
            for table in self.table:
                if table.guest != None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                    if not self.queur.empty():
                        table.guest = self.queur.get()
                        print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        table.guest.start()

tables: list[Table] = [Table(number) for number in range(1, 5)]
guests_names: list[str] = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests: list[Guest] = [Guest(name) for name in guests_names]
cafe = Cafe(tables)
cafe.guest_arrival(guests)
cafe.discuss_guests()