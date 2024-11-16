from multiprocessing import Pool
from time import time

def read_info(name) -> list:
    all_data: list = []
    with open(f"./module_10_5/{name}", encoding='utf-8') as file:
        line = file.readline().rstrip('\n')
        while line:
            all_data.append(line)
            line = file.readline().rstrip('\n')
    return all_data

    
file_name: list[str] = [f'file {n}.txt' for n in range(1, 5)]


def line_call(): 
   time_start: float = time()
   for name in file_name:
      print(f"{name}")
      read_info(name)
   time_end: float = time() - time_start
   print(f"{time_end} линейный вызов")

def multiprocess_call():
    time_start: float = time()
    with Pool(4) as pool:
        pool.map(read_info, file_name)
    time_end: float = time() - time_start
    print(f"{time_end} многопоточный вызов")

   

if __name__ == '__main__':
    # line_call()
    multiprocess_call()