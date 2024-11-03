from random import choice
from typing import Any

first: str = 'Мама мыла раму'
second: str = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))

def get_advanced_writer(file_name: str):
    if not isinstance(file_name, str):
        raise TypeError("Название файла должно быть строкой")
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write('\n'.join(map(str, data_set)))
    return write_everything

#можно так
# get_advanced_writer('module_9_4.txt')('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#а можно и так
write = get_advanced_writer('module_9_4.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *words: str) -> None:
        self.__is_valid_type(words)
        self.__words: tuple = words

    def __is_valid_type(self, words: tuple) -> bool:
        for word in words:
            if not isinstance(word, str):
                raise TypeError("Передаваемые данные должны быть строкой")
    
    def __call__(self) -> str:
        return choice(self.__words)

#можно так 
print(MysticBall('Да', 'Нет', 'Наверное')())

#а можно и так
mb = MysticBall('Да', 'Нет', 'Наверное')
print(mb())
print(mb())
print(mb())