from os import path

class WordsFinder:
    """
    Класс для поиска слов в фалах, а так же для подсчёта количества слов в фале.
    Поиск осуществляется в директории, которая указывается в параметре file_path.
    По умолчанию указана директория "module_7_3".
    Обязательный аргумент при создании экземпляра класса  - имена файлов в которых будет производиться поиск
    """
    def __init__(self, *files: tuple, file_path: str = "module_7_3/") -> None:
        self.__files = files
        self.__file_path = file_path
        self.__valid()

    def __valid(self):
        for file in self.__files:
            if not file.endswith(".txt"):
                raise ValueError(f"Файл {file} не является текстовым")

    # метод для получения списка слов в открываемом фале
    def __string_to_list(self, string: str) -> list:
        string = string.replace("\n", " ") # удаляем переносы строк
        for mark in (',', '.', '=', '!', '?', ';', ':', ' - '):
            string = string.replace(mark, "") # удаляем знаки препинания
        return string.lower().split()

    def __get_all_words(self) -> dict:
        all_words = {}
        for file in self.__files:
            # проверка наличия файла в директории
            if not path.exists(self.__file_path + file):
                print(f"Файл {file} в директории {self.__file_path} не найден")
                continue
            with open(self.__file_path + file, encoding="utf-8") as f:
                all_words[file] = self.__string_to_list(f.read())
        return all_words

    def find(self, word: str) -> dict:
        dict_find_words = {}
        for find_file, find_word in self.__get_all_words().items():
            if word.lower() in find_word:
                dict_find_words[find_file] = find_word.index(word.lower())
        return dict_find_words
    
    def count(self, word: str) -> dict:
        dict_find_words = {}
        for find_file, find_word in self.__get_all_words().items():
            if word.lower() in find_word:
                dict_find_words[find_file] = find_word.count(word.lower())
        return dict_find_words
     
    
wf = WordsFinder("fake_file.txt", "products.txt", "test_tell.txt")

print(wf.count('ОвОщи'))
print(wf.find('СпасиБо'))

