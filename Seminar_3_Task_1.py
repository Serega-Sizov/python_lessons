# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1

import random

num = int(input('Введите количество элементов в массиве: '))
chislo = int(input('Какое число вы хотите проверить?: '))
list_numbers = []
for i in range(num):
    list_numbers.append(random.randint(0, 3))
# print(list_numbers)
count = 0
for i in range(len(list_numbers)):
    if chislo == list_numbers[i]:
        count += 1
print(f'Число {chislo} в списке {list_numbers} встречается {count} раз')