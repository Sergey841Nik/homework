def test_function():
    def inner_function():
        return "Я в области видимости функции test_function"
    print(inner_function())

test_function()

try:
    inner_function()
except NameError:
    print("inner_function не определена в глобальной области видимости")