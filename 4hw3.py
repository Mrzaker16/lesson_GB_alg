"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit
import cProfile



def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num, revers_num=" "):
    enter_num = str(enter_num)
    for i in range(len(enter_num)):
        revers_num = revers_num + enter_num[(len(enter_num) - 1) - i]
    return revers_num


enter_num = int(input('Введите целое число: '))

revers_1(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)
revers_4(enter_num, revers_num=" ")

print(
    'Число наоборот на рекурсиях: ',
    timeit(
        f'revers_1(enter_num)',
        globals=globals(),
        number=10000))
print(
    'Число наоборот на цикле while: ',
    timeit(
        f'revers_2(enter_num)',
        globals=globals(),
        number=10000))
print(
    'Число наоборот на срезах: ',
    timeit(
        f'revers_3(enter_num)',
        globals=globals(),
        number=10000))
print(
    'Число наоборот на цикл for: ',
    timeit(
        f'revers_3(enter_num)',
        globals=globals(),
        number=10000))


cProfile.run('revers_1(10000000000)')
cProfile.run('revers_2(10000000000)')
cProfile.run('revers_3(10000000000)')
cProfile.run('revers_4(10000000000)')



'''
Наиболее быстрая функция является разворот через срезы O(b-a).
На втором месте по скорости исполнения:
 При маленьком количестве элементов!!!
 цикл WHILE пока число не будет равно 0,
 остаток от целочисленного деления на 10 записывается в новую переменную,
  а исчисляемое сокращается на один порядок. O(n)
При большом количестве элементов
 на втором месте ЦИКЛ FOR... IN... со сложностью O(n)

 Последнее место по производительности это РЕКУРСИВНАЯ функция
  с экспонинциальной сложностью сложность O(2**n)
Вычисления для числа длиной 38 цифр

Число наоборот на рекурсиях:  0.014560600000000257
Число наоборот на цикле while:  0.008457500000000007
Число наоборот на срезах:  0.004393400000000103
Число наоборот на цикл for:  0.004680399999999807
'''