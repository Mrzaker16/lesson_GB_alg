"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
"""



from time import time

create_list = []
create_dict = {}
n = 10 ** 5

def time_decorator(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполенения функции {func.__name__} '
              f'составило {end - start}')
        return result

    return timer


@time_decorator
def fill_list(lst, num):
    for i in range(num):            #O(1)
        lst.append(i)               #O(1)


fill_list(create_list, n)



@time_decorator
def fill_dict(dict, num):
    for i in range(num):        #O(1)
        dict[i] = i             #O(1)


fill_dict(create_dict, n)


# Время выполенения функции fill_list составило 0.007985353469848633
# Время выполенения функции fill_dict составило 0.008930206298828125



"""
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.
   Операцию clear() не используем.
"""

@time_decorator
def pop_list(list):
    for i in range(10000):          #O(1)
        list.pop(i)                 #O(1)


pop_list(create_list)


@time_decorator
def pop_dict(dict):
    for i in range(100):            #O(1)
        dict.pop(i)                 #O(1)



pop_dict(create_dict)


#Вывод в обоих случаях быстрее будет словарь




