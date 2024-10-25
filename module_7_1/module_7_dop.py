class Context:
    def __init__(self):
        self.__values: tuple = ()

    def __enter__(self) -> list:
        self.__values = list(self.__values)
        return self.__values
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None: #если не было исключений
            self.__values = tuple(self.__values)
        return self.__values

    def __str__(self) -> str:
        return str(self.__values)
    
cx = Context()
print(cx)

with cx as x:
    x.append(2)
    print(x)

print(cx)