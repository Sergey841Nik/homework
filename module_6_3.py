class Horse:
    def __init__(self):
        # super().__init__() #т.к. непосредственно в классе Pegasus мы вызываем инициализатор Eagl, этот super() не нужен
        self.x_distance = 0 
        self.sound = 'Frrr'
    
    def run(self, dx):
        self.x_distance += dx
        return self.x_distance

class Eagle:
    def __init__(self):
        self.y_distance = 0 
        self.sound = 'I train, eat, sleep, and repeat'
    
    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__() #тут можно и Horse.__init__(self), но с сделаем так, чтобы хотябы от имени первого базового класса независить  
        Eagle.__init__(self) #атрибут sound класса Eagle переопределён одноимённым атрибутом класса Horse (потому как Horse в цепочке mro стоит перед Eagle)
                            #поэтому "достучатся" до него предлагаю именно так. Если есть другой способ (с использованием super()) пожалуйста подскажите
    def get_pos(self):
        return self.x_distance, self.y_distance
    
    def voice(self):
        return self.sound
    
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)


def main():
    pg = Pegasus()
    print(pg.voice())

    pg.move(10, 10)
    print(pg.get_pos())
    pg.move(-5, 10)
    print(pg.get_pos())


if __name__ == '__main__':
    main()






    