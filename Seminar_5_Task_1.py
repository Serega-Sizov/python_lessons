# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

number = int(input('Введите число: '))
degree = int(input('Введите степень: '))


def number_in_degree(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 == 0:
        h = pow(a, b // 2)
        return h * h
    else:
        h = pow(a, (b-1) // 2)
        return a * h * h


res = number_in_degree(number, degree)
print(f'Число {number} в степени {degree} равно {res}')
