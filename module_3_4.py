# 1-й
def single_root_words(root_words, *other_words):
    some_words = []
    for word in other_words:
        if word.lower() in root_words.lower() or root_words.lower() in word.lower():
            some_words.append(word)
    return some_words


print(single_root_words("Disablement", "Able", "Mable", "Disable", "Bagel"))
print(single_root_words("Тор", "Квадрат", "ПоВтОр", "Ор", "Огурец", "экватоР"))


# 2-й с count
def single_root_words_s_count(root_words, *other_words):
    some_words = []
    for word in other_words:
        if (
            root_words.lower().count(word.lower()) > 0
            or word.lower().count(root_words.lower()) > 0
        ):
            some_words.append(word)
    return some_words


print(single_root_words_s_count("Disablement", "Able", "Mable", "Disable", "Bagel"))
print(single_root_words_s_count("Тор", "Квадрат", "ПоВтОр", "Ор", "Огурец", "экватоР"))