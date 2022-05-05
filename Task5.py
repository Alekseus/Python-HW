# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов (нет нулевых кофициентов).

import numpy as np
import os
import re

with open('1_Polynomial.txt', 'r') as f:
    poly = f.read()

with open('2_Polynomial.txt', 'r') as f:
    poly2 = f.read()


def ratio(poly):
    f = re.findall(r'\d+', poly)
    a = f[::2]
    a.pop()
    a.append(f[-2])
    a = [int(i) for i in a]
    return a

def ratio2(poly2):
    f = re.findall(r'\d+', poly2)
    b = f[::2]
    b.pop()
    b.append(f[-2])
    b = [int(i) for i in b]
    return b


p1 = np.poly1d(ratio(poly))
p2 = np.poly1d(ratio2(poly2))
p3 = np.polyadd(p1, p2)

sum_poly = (f'{p3} = 0')
print(sum_poly)

with open('3_Polynomial.txt', 'w') as f:
    f.write(sum_poly)


