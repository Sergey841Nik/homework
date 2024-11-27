
def introspection_info(obj) -> dict:
    # Получаем базовую информацию об объекте
    result: dict = {
        'Тип объекта': type(obj),
        'Все атрибуты и методы объекта': dir(obj)
    }
        
    # Получение списка методов
    methods: list[str] = [attr for attr in dir(obj) if callable(getattr(obj, attr)) and not attr.startswith('__')]
    result['Методы объекта'] = methods

    # Получение атрибутов
    result['Атрибуты объекта'] = obj.__dict__

    # Получение модуля, к которому относится объект
    module = getattr(obj, '__module__', None)
    if module is not None:
        result['Модуль'] = module
    
    return result

class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name: str = name
        self.number_of_floors: int = number_of_floors

    def go_to(self, new_floor: int):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor+1):
                print(floor)
        else:
            print("Такого этажа не существует")

hs = House('ЖК', 3)

print(introspection_info(hs))