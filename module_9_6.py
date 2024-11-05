
def all_variants(text):
    n = 1
    while n <= len(text):
        i = 0
        j = n
        while j <= len(text):
            yield text[i:j]
            i += 1
            j += 1
        n += 1

for i in all_variants('abc'):
    print(i)