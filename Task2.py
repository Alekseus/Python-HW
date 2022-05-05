# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число N: '))

def list(n):
    list_simple = []
    simple = 2
    while n > 1:
        if not n % simple:
            list_simple.append(simple)
            n = n/simple
        else:
            simple += 1
    print(list_simple)

list(n)