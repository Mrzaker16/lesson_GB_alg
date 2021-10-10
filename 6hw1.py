"""
Задание 1.
Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""


from memory_profiler import profile
from pympler import asizeof
from timeit import timeit




@profile
def decor(func):                                                    # 0
    def wrapper(*argv):                                             # 0
        return func(*argv)                                          # 0
    return wrapper                                                  # 0

@ decor
def get_rev_number(number, rev_number = ''):                        # 0
!
    if number == 0:                                                 # 0
        return rev_number                                           # 0
    else:

        last_number = number % 10                                   # 0
        rev_number += str(last_number)                              # 0
        return get_rev_number(number // 10, rev_number)             # 0.2

@profile
def get_rev_number_2(number, rev_number = ''):                      # 0
    while number != 0:                                              # 0
        last_number = number % 10                                   # 0
        rev_number += str(last_number)                              # 0
        number = number // 10                                       # 0
    return rev_number                                               # 0

number_s = 1230
print(get_rev_number(number_s))
print(get_rev_number_2(number_s))
print(timeit("get_rev_number(number_s)", setup="from __main__ import get_rev_number, number_s", number=1000000))
print(timeit("get_rev_number_2(number_s)", setup="from __main__ import get_rev_number_2, number_s", number=1000000))

'''
1 000 000 повторений:
get_rev_number = 1.291
get_rev_number_2 = 1.012
Аналитика:
Замена Рекурсии на Цикл привела к снижению сложности и увеличению скорости 
обработки операций с факториальной O(n!) на линейную O(n).
@profile - показывает, что цикл не нагружает доп. элементы в Increment - что говорит о том,
 что дополнительной Опертивной памяти для хранения Итерации не требуется. 
'''



class HexNumber:
    def __init__(self, num_1,num_2):
        self.num_1 = num_1
        self.num_2 = num_2


simple_int_1 = '1a3'
simple_int_2 = '3de'
a = HexNumber(simple_int_1, simple_int_2)
print(asizeof.asizeof((a)))                                     # asizeof.asizeof = 376

class HexNumber:
    __slots__ = ('num_1', 'num_2')
    def __init__(self, num_1,num_2):
        self.num_1 = num_1
        self.num_2 = num_2


simple_int_1 = '1a3'
simple_int_2 = '3de'
a = HexNumber(simple_int_1, simple_int_2)
print(asizeof.asizeof((a)))                                     # asizeof.asizeof = 160

"""
Аналитика:
Использование __slots__ приводит к изменению типа данных для хранения.
По умолчанию используется dict, и так как его идентификаторы/ключи ХЕШируются,
данные занимают вдвое больше памяти, например, по сравнению с tuple!
asizeof.asizeof = 376 без использования __slots__
asizeof.asizeof = 160 с использования __slots__
"""

@profile
def simple_alg(i):
    """Перебор делителей"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


@profile
def eratosfen_alg(i):
    """Решето Эратосфена"""
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1

    return [p for p in sieve if p != 0][i-1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple_alg(i))
print(eratosfen_alg(i))


""" 
Незначительный инкремент Решета обусловлен необходимостью генерации списка.
Величина инкремента может изменяться, в зависимости от объема списка.
При этом в целом инкремент находится в рамках нормы.
Оптимизация не требуется.
"""
