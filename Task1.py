# Вычислить число Пи c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$
import math

import math

a = int(input('Введите необходимое число знаков после запятой в числе pi: '))

d = 10**(-a)
print(f'Заданная точность: {d}')
print(f'{math.pi:.{a}f}')