calls = 0


class ListStringLower:
    def __init__(self):
        pass

    def __call__(self, *args):
        lst = []
        for i in args[0]:
            lst.append(i.lower())
        return lst


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string: str):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string: str, list_to_search: list[str]):
    count_calls()
    lst_low = ListStringLower()
    if string.lower() in lst_low(list_to_search):
        return True
    return False


print(string_info("Помидор"))
print(is_contains("ПоМиДор", ["Помидор", "МиДор"]))
print(is_contains("Огурец", ["Гурец", "огур"]))
print(calls)
