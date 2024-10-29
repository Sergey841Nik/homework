import re

class IncorrectVinNumber(Exception):
    """
    Класс исключений для Vin номера автомобиля
    """
    def __init__(self, message: str) -> None:
        self.message = message if message else None

    def __str__(self) -> str:
        return self.message
    
class IncorrectCarNumbers(Exception):
    """
    Класс исключений для госномера автомобиля
    """
    def __init__(self, message: str) -> None:
        self.message = message if message else None

    def __str__(self) -> str:
        return self.message
    
#проверку на тип передаваемых данных вынес в отдельный класс
class IncorrectTypesInfjCar(Exception):
    """
    Класс исключений для типа передаваемых данных
    """
    def __init__(self, message: str) -> None:
        self.message = message if message else None

    def __str__(self) -> str:
        return self.message
    
class Car:
    def __init__(self, model: str, vin_number: int, car_number: str) -> None:
        self.model = model
        self.__vin = vin_number
        self.__numbers = car_number
        self.__is_valid_type(self.model, self.__vin, self.__numbers)
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)


    def __is_valid_type(self, *args)-> None:
        if not isinstance(args[0], str):
            raise IncorrectTypesInfjCar('Некорректный тип названия модели')
        elif not isinstance(args[1], int):
            raise IncorrectTypesInfjCar('Некорректный тип vin номер')
        elif not isinstance(args[2], str):
            raise IncorrectTypesInfjCar('Некорректный тип данных для номеров',)
        
    def __is_valid_vin(self, vin_number)-> None:
        if not 1_000_000 <= vin_number <= 9_999_999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        
    def __is_valid_numbers(self, numbers)-> None:
        #создаём шаблон для госномера, без учёта регистра
        pattern = r'^[а-яА-Я]\d{3}[а-яА-Я]{2}$'
        if not re.match(pattern, numbers): #проверяем переданный номер на соответствие шаблону, в том числе проверяет длину строки
            raise IncorrectCarNumbers('Неверная длина номера или формата принятого в РФ')
        
    def __str__(self) -> str:
        return f" Автомобиль - {self.model}, VIN - {self.__vin}, госномер - {self.__numbers}"


print(Car('Reno', 5_058_958, 'а582бр'))
# print(Car(123, 5_058_958, 'а582бр'))
# print(Car('Reno', 5_058_9580, 'а582бр'))
print(Car('Reno', '5_058_958', 'а582бр'))
# print(Car('Reno', 5_058_958, 'а582б5'))
        
        
