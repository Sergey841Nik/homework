my_dict: dict = {"Огурцы": 55, "Картофель": 100, "Помидоры": 150}
print(my_dict)
print(my_dict["Огурцы"], my_dict.get("Лопата"), sep="\n")
my_dict.update({"Капуста": 500, "Морковь": 600})
my_tomatoes = my_dict.pop("Помидоры")
print(my_tomatoes)
print(my_dict)

my_set: set = {1, 2, 3, 1, "Огурцы", (1, 2, 3), (1, 2, 3)}
print(my_set)
my_set.add(4), my_set.add("Помидоры")
my_set.discard(2)
print(my_set)
