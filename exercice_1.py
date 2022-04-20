

my_list = [14, 5, 14, 8, 14, 15, 6, 2, 1]

value_to_get = 14  # The required element


def get_index(my_list, value_to_get):
    pos = []
    for i in range(len(my_list)):
        if my_list[i] == value_to_get:
            pos.append(i)
    return pos


print(get_index(my_list, value_to_get))
