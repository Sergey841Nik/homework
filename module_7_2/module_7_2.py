

def custom_write(file_name: str, lst_for_strings: list) -> dict:
    file = open(f"module_7_2/{file_name}", 'w', encoding= 'utf-8')
    strings_positions = {}
    for num_string, string in enumerate(lst_for_strings, 1): 
        key = num_string, file.tell()
        file.write(string + '\n')
        strings_positions[key] = string
    file.close()
    return strings_positions


info = [
    "Text for tell.",
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

print(custom_write('test_tell.txt', info))
