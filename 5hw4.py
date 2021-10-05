"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""


from timeit import timeit
from collections import OrderedDict

dict = {1: 'one', 2: 'two', 3: 'three'}
ordict = OrderedDict(dict)

def dict_fill():
    for i in range(4,7):
        dict[i] = chr(93 + i)
    return dict

def ordict_fill():
    for i in range(4,7):
        ordict[i] = chr(93 + i)
    return ordict

def dict_get():
    dict.get(3)
    return dict

def ordict_get():
    ordict.get(3)
    return ordict

print(
    timeit(
        "dict_fill()",
        setup="from __main__ import dict_fill", number=1000))

print(
    timeit(
        "ordict_fill()",
        setup="from __main__ import ordict_fill", number=1000))

print(
    timeit(
        "dict_get()",
        setup="from __main__ import dict_get", number=1000))

print(
    timeit(
        "ordict_get()",
        setup="from __main__ import ordict_get", number=1000))
'''
Обычный словарь заполняется элементами быстрее, чем OrderedDict. 
Это связано прежде всего с тем, что:
1. OrderedDict реализован на Python, а обычный словарь на С 
и априори должен работать быстрее.
2. OrderedDict был разработан для быстрого переупорядочивания элементов, 
а производительность в части заполнения вторична.
'''

'''
Для 1000 повторов:
Заполнение:
dict_fill - 0.0008742999999999945
ordict_fill - 0.0009874999999999953
Получение элемента:
dict_get - 0.00016220000000000123
ordict_get - 0.00016440000000000204
Тип данных OrderedDict после Python3.6 потерял актуальность так как ключи-значения class 'dict' 
перестали при выводе данных носить неупорядоченный характер.
'''