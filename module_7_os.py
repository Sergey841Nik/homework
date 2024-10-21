import os
import time


def search_file(search_dir: str):
    path_for_search = os.path.abspath(search_dir)

    for adres, dirs, files in os.walk(path_for_search):
        for file in files:
            # используем функцию генератор. Она не хранит все найдены элементы в памяти, а "достаёт" их при очередном запросе
            yield os.path.join(adres, file)


def print_search_results(path_for_search) -> None:
    for file in search_file(path_for_search):
        found_file = os.path.basename(file)
        found_path_to_file = os.path.dirname(file)
        time_last_modification_file_seconds = os.path.getmtime(file)
        time_last_modification_file_tuple = time.localtime(
            time_last_modification_file_seconds
        )
        time_last_modification_file = time.strftime(
            "%d.%m.%Y %H:%M", time_last_modification_file_tuple
        )
        size_found_file = os.path.getsize(file)
        print(
            f"Обнаружен файл: {found_file}, Путь: {found_path_to_file}, Размер: {size_found_file} байт, Время изменения: {time_last_modification_file}"
        )


path_for_search = input(
    "Укажите директорию в которой будем искать файлы\nесли это текущая директория то поставе точку\n"
)
print_search_results(path_for_search)
