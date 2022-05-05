# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 1 до 100, можно создать свой генератор случайных чисел или использовать готовый) многочлена
# и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0

from random import randint
import itertools
import os

k = int(input('Задайте натуральную степень k: '))

def get_rat(k):
    ratio = [randint(1, 100) for i in range (k + 1)]
    while ratio[0] == 0:
        ratio[0] = randint(1, 10)
    return ratio

def get_polynom(k, ratio):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratio, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')

ratio = get_rat(k)
polynom1 = get_polynom(k, ratio)
print(polynom1)

with open('2_Polynomial.txt', 'w') as f:
    f.write(polynom1)