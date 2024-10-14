from math import sqrt, pi

class Figure:
    """
    Класс для работы с геометрическими фигурами.
    Первым атрибутом передаётся color в формате (r, g, b).
    Далее передаётся произвольное количество сторон.
    Если количество сторон не соответствует количеству 
    сторон геометрической фигуры то возвращается фигура 
    с единичной стороной.
    """

    SIDES_COUNT = 0
    def __init__(self, color: tuple[int], *sides) -> None:
        self.__color = color
        self.__sides = sides
        self.filled = False
        self.set_color(self.__color)
        self.set_sides(self.__sides)

    def __is_valid_color(self, color: tuple[int]) -> bool:# проверка на корректность цвета
        if len(color) != 3:
            raise ValueError("Цвет должен передаваться в формате (r, g, b)")
        r, g, b = color
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            self.filled = True # если все введено верно то фигура закрашена
            return True
        else:
            return False

    def __is_valid_filled(self)-> str:
        if self.filled:
            return f"Фигура закрашена в цвет {self.__color}"
        return "Фигура не закрашена, возможно некорректно введена цвет"
    
    def __is_valid_sides(self, sides: tuple[int]) -> bool:
        if len(sides) != self.SIDES_COUNT: # проверка на корректность количества сторон
            return False
        return True
    
    def get_color(self) -> str:
        return self.__is_valid_filled()
    

    def set_color(self, *new_color) -> None: # установка цвета
        if isinstance(new_color[0], tuple): #проверяем на вложенность и достаём вложенный кортеж
            new_color = new_color[0]
        if self.__is_valid_color(new_color): # проверка на корректность цвета
            self.__color = new_color # установка нового цвета
    
    def get_sides(self) -> tuple[int]:
        return self.__sides # возвращение кортеж сторон
    
    def set_sides(self, *new_sides) -> None: # установка сторон
        if isinstance(new_sides[0], (tuple, list)): #проверяем на вложенность и достаём вложенный кортеж или список
            new_sides = new_sides[0]
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)
        else:
            self.__sides = [1] * self.SIDES_COUNT 

    def __len__(self) -> int:
        return sum(self.__sides) #определение периметра фигуры
    

class Circle(Figure):
    """
    Класс для работы с геометрической фигурой круг,
    класс наследуется от класса Figure.
    В качестве длины стороны передаётся длина окружности.
    Далее определяется радиус круга и площадь круга.
    """

    SIDES_COUNT = 1
    def __init__(self, color: tuple[int], *sides) -> None:
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self) -> float: 
        return round(pi * self.__radius ** 2, 2) # вычисление площади круга

class Triangle(Figure):
    """
    Класс для работы с геометрической фигурой треугольник,
    класс наследуется от класса Figure и определяет площадь треугольника
    """
    SIDES_COUNT = 3
    def get_square(self) -> float: # вычисление площади треугольника
        p = len(self) / 2
        print(p)
        mult1 = p - self.get_sides()[0]
        mult2 = p - self.get_sides()[1]
        mult3 = p - self.get_sides()[2]
        print(mult1, mult2, mult3)
        return round(sqrt(p * mult1 * mult2  * mult3), 2)
    
class Cube(Figure):
    """
    Класс для работы с геометрической фигурой куб,
    класс наследуется от класса Figure и определяет объём куба.
    В параметр sides передаётся одно значение т.к. куб равносторонняя фигура
    """
    SIDES_COUNT = 12

    def __init__(self, color: tuple[int], *sides) -> None:
        self.__sides = list(sides) * 12 # переопределяем атрибут экземпляра класса
        super().__init__(color, *self.__sides) # передаём переопределённый атрибут
        
    def set_sides(self, *new_sides) -> None: # переопределяем метод
        new_sides = list(new_sides) * 12
        return super().set_sides(*new_sides)
    
    def get_volume(self) -> float: # вычисление объёма куба
        return self.get_sides()[0] ** 3

def circle():
    cl = Circle((256, 0, 0), 10)
    print(cl.get_color())
    cl.set_color(255, 255, 255)
    print(cl.get_color())
    print(cl.get_square())
    cl.set_sides(10, 20, 30)
    print(cl.get_sides())
    print(len(cl))

def triangle():
    tr = Triangle((0, 0, 0), 10)
    print(tr.get_color())
    print(tr.get_sides())
    tr.set_color(258, 255, 255)
    print(tr.get_color())
    print(tr.get_square())
    tr.set_sides(30, 20, 30)
    print(tr.get_sides())
    print(tr.get_square())
    print(len(tr))

def cube():
    cb = Cube((50, 60, 255), 10)
    print(cb.get_color())
    print(cb.get_sides())
    cb.set_color(258, 255, 255)
    print(cb.get_color())
    print(cb.get_volume())
    cb.set_sides(30)
    print(cb.get_sides())
    print(cb.get_volume())
    print(len(cb))

if __name__ == "__main__":
    # circle()
    # triangle()
    cube()

