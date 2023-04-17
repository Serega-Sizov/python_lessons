# Задача 18:
# Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5
import random
num_for_list = int(input('Введите количество элементов в списке: '))
num = int(input('Введите число ближайшее к которому нужно найти?: '))
num_list = []

for i in range(num_for_list):
    num_list.append(random.randint(1, 20))
print(num_list)

min_num = abs(num-num_list[0])
index = 0
for i in range(1, num_for_list):
    count = abs(num - num_list[i])
    if count < min_num:
        min_num = count
        index = i
print(f'Ближайшее число к числу {num} равно {num_list[index]}')
