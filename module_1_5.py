immutable_var: tuple = (1, 2, 3, "Огурцы", "Помидоры")

print(immutable_var)

try:
    immutable_var[3] = "Капуста"
except TypeError:
    print("Нельзя изменить элемент кортежа, потому как он неизменяемый тип")

mutable_list: list = [1, 2, 3, "Огурцы", "Помидоры"]
mutable_list.append("Капуста")
print(mutable_list)

mutable_list[0], mutable_list[-1] = mutable_list[-1], mutable_list[0]
print(mutable_list)

mutable_list.pop(0)
mutable_list.pop()
print(mutable_list)

# И хватит пожалуй
