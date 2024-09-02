my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

len_my_list = len(my_list)
n = 0

while n < len_my_list:
    if my_list[n] > 0:
        print(my_list[n])
    elif my_list[n] < 0:
        break
    n += 1
