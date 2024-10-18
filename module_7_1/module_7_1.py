import os

class Product:
    def __init__(self, name: str, weight: float | int, category: str) -> None:
        self.name = name
        self.weight = weight
        self.category = category

    def __verif_type(self) -> bool:
        if not isinstance(self.name, str) and isinstance(self.weight, (float, int)) and isinstance(self.category, str):
            # если не все данные введены правильно, то выводим сообщение об ошибке
            raise TypeError(f"Некорректный тип данных: {self.name}, {self.weight}, {self.category}")

    def __str__(self) -> str:
        return f"{self.name}, {self.weight}, {self.category}"
    

class Shop:
    def __init__(self) -> None:
        self.__file_name = "products.txt"

    def __open_file(self, prod: Product) -> str | None:
        if prod:
            # "обернём" в обработчик исключений, чтобы в случае в возникновения оной фаил всё равно был бы закрыт
            try: 
                # открываем файл для записи. Кодировка utf-8
                file = open(f"module_7_1/{self.__file_name}", "a", encoding="utf-8")  
                file.write(f"{prod}\n")
            except Exception as e:
                # если файл не открыт, то выводим сообщение об ошибке
                print(f"Ошибка при открытии файла: {e}")
            finally:
                #finally отрабатывает всегда поэтому тут закрываем файл
                file.close() 
                return None
        try:
            # открываем файл для чтения. Кодировка utf-8
            file = open(f"module_7_1/{self.__file_name}", 'r', encoding="utf-8")
            res_list = [prod.strip('\n') for prod in file]
        except Exception as e:
            print(f"Ошибка при открытии файла: {e}")
        finally:
            file.close()
            return '\n'.join(res_list)
        
    def __get_product_from_file_from_verif(self, name: str) -> bool:
        products_in_file = self.products.split('\n')
        for info_product in products_in_file:
            if name == info_product.split(',')[0]:
                return True
        return False

    @property #применяем этот декоратор, чтобы работать с методами как с атрибутами, для метода get(взять что-то) и set(записать что-то)
    def products(self) -> str:
        # проверяем, существует ли файл
        if not os.path.exists(f"module_7_1/{self.__file_name}"):
            return ""
        # получаем данные из файла
        return self.__open_file(None)
    
    @products.setter
    def products(self, *args: Product) -> None:
        if isinstance(args[0], tuple):
            args= args[0]
        else:
            args = args

        for prod in args:
            # проверяем, есть ли продукт c таким именем в файле
            if self.__get_product_from_file_from_verif(prod.name):
                print(f"Подукт {prod.name} уже существует")
            else:
                # если нет, то записываем в файл
                self.__open_file(prod)
                print(f"Подукт {prod.name} добавлен")
        
def main()-> None:
    shop = Shop()
    pr1 = Product("Огурцы", 150.5, "Овощи")
    pr2 = Product("Капуста", 100, "Овощи")
    pr3 = Product("Гвозди", 205.6, "Строительные товары")
    pr4 = Product("Картофель", 200, "Овощи")

    shop.products = pr1, pr2, pr3
    print(shop.products)
    print('-' * 20)
    shop.products = pr4
    print(shop.products)




if __name__ == "__main__":
    main()

        




