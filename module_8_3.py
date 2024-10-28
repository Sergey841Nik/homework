import re

class IncorrectVinNumber(Exception):
    """
    Класс исключений для Vin номера автомобиля
    """
    def __init__(self, *args) -> None:
        self.message = args[0] if args else None

    def __str__(self) -> str:
        return f"Неверный диапазон для Vin номера {self.message}"
    
class IncorrectCarNumbers(Exception):
    """
    Класс исключений для госномера автомобиля
    """
    def __init__(self, *args) -> None:
        self.message = args[0] if args else None

    def __str__(self) -> str:
        return f"Госномер {self.message} не соответствует принятому в РФ шаблону"
    
class IncorrectTypesInfjCar(Exception):
    """
    Класс исключений для типа передаваемых данных
    """
    def __init__(self, *args) -> None:
        self.message = args[0] if args else None

    def __str__(self) -> str:
        return f"Неверный тип {self.message}"
    
class Car:
    def __init__(self, model: str, vin_number: int, car_number: str) -> None:
        self.model = model
        self.__vin = vin_number
        self.__numbers = car_number
        self.__is_valid_type(self.model, self.__vin, self.__numbers)
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_type(self, *args)-> None:
        if not isinstance(self.model, str):
            raise IncorrectTypesInfjCar('модели')
        elif not isinstance(self.__vin, int):
            raise IncorrectTypesInfjCar('vin номера')
        elif not isinstance(self.__numbers, str):
            raise IncorrectTypesInfjCar('госномера')
        
    def __is_valid_vin(self, vin_number)-> None:
        if not 1_000_000 <= vin_number <= 9_999_999:
            raise IncorrectVinNumber(vin_number)
        
    def __is_valid_numbers(self, numbers)-> None:
        #создаём шаблон для госномера, без учёта регистра
        pattern = r'^[а-яА-Я]\d{3}[а-яА-Я]{2}$'
        if not re.match(pattern, numbers): #проверяем переданный номер на соответствие шаблону
            raise IncorrectCarNumbers(numbers)
        
    def __str__(self) -> str:
        return f" Автомобиль - {self.model}, VIN - {self.__vin}, госномер - {self.__numbers}"


print(Car('Reno', 5_058_958, 'а582бр'))
# print(Car(123, 5_058_958, 'а582бр'))
# print(Car('Reno', 5_058_9580, 'а582бр'))
# print(Car('Reno', '5_058_958', 'а582бр'))
print(Car('Reno', 5_058_958, 'а582б5'))
        
        
