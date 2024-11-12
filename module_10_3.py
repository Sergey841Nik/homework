from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self, balance: int) -> None:
        self.balance = balance
        self.__lock = Lock()

    def deposit(self) -> None:
        for _ in range(100):
            change_balance: int = randint(50, 500)
            self.balance += change_balance
            print(f"Пополнение: {change_balance}. Баланс: {self.balance}")
            if self.__lock.locked() and self.balance >= 500:
                self.__lock.release()
            sleep(0.001)

    def take(self) -> None:
        for _ in range(100):
            change_balance: int = randint(50, 500)
            print(f"Запрос на {change_balance}")
            if self.balance >= change_balance:
                self.balance -= change_balance
                print(f"Снятие: {change_balance}. Баланс: {self.balance}")
            else:
                self.__lock.acquire()
                print("Запрос отклонён, недостаточно средств")
            sleep(0.001)

bk = Bank(100)

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")
