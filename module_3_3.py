def print_params(a=1, b="строка", c=True):
    return f"a = {a}, b = {b}, c = {c}"


print(
    print_params(),
    print_params(c=[1, 2, 3]),
    print_params(b=25),
    print_params(a=True, b=[1, 2, 3], c="что-то написано"),
    sep="\n",
)
print("*" * 20)

values_list = ["value", False, [1, 2, 3]]
values_dict = {"a": True, "b": "Строка", "c": [11, 22, 33]}


def print_params(a, b, c):
    return f"a = {a}, b = {b}, c = {c}"


print(print_params(*values_list))
print(print_params(**values_dict))

values_list_2 = [250, 'Сентябрь']

print(print_params(*values_list_2, 42))