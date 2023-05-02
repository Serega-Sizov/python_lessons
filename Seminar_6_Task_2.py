# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

num_list = [random.randint(1,100) for i in range(10)]
print(num_list)
# Мы хотим найти индексы элементов списка, которые находятся в диапазоне от 30 до 50.
num_min = 30
num_max = 50
index = []

for item in range(len(num_list)):
    if num_min <= num_list[item] <= num_max:
        index.append(item)

print(index)
