class Context:
    def __init__(self):
        self.__values: tuple = ()

    def __enter__(self) -> list:
        self.__values_copy = list(self.__values)
        return self.__values_copy
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is None: #если не было исключений
            self.__values = tuple(self.__values_copy)
        
        
    def __str__(self) -> str:
        return str(self.__values)
    
cx = Context()
print(cx)

with cx as x:
    x.append(2)

print(cx)

try:
    with cx as x:
        x.append(2)
        kjkj
except Exception:
    pass

print(cx)

with cx as x:
    x.append(22)

print(cx)
