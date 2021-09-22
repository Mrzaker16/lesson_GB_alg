# Задание 2.


# Сложность O(n**2)
def get_min_number_1(lst):
    min_number_2 = lst[0]                                   # O(1)
    for i in lst:                                           # O(n)
        for j in range(lst.index(i) + 1, len(lst) - 1, 1):  # O(n)
            if min_number_2 > lst[j]:                       # O(n)
                min_number_2 = lst[j]                       # O(1)
    return min_number_2                                     # O(1)


# сложность O(n)
def get_min_number_2(lst):
    min_number = lst[0]                                     # O(1)
    for i in lst:                                           # O(n)
        if i < min_number:                                  # O(n)
            min_number = i                                  # O(1)
    return min_number                                       # O(1)


first_list = [600, 30, 10, 8, 1, 5]

print(get_min_number_1(first_list))

print(get_min_number_2(first_list))