from time import sleep, time
from threading import Thread

def write_words(word_count: int, file_name: str) -> None:
    with open(f"module_10_1/{file_name}", 'w', encoding='utf-8') as file:
        for word in range(1, word_count + 1):
            file.write(f"Какое-то слово №{word}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

start_time = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time() - start_time
print(f"Работа функции в одном потоке {end_time:.3f} секунд")

threads: list = []

for count, filename in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = Thread(target=write_words, args=(count, filename))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time_threads = time() - start_time - end_time
print(f"Работа функции в переключающихся потоках {end_time_threads:.3f} секунд")