# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N)
# 0! = 1
# Решить задачу используя цикл while

# n = int(input('Введите число: '))
# fact = 1
# count = 1

# while count <= n:
#     fact *= count
#     count += 1

# print(fact)

# ------------------------------------------------------------------------------------------------------------------------

# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.
n1 = 0
n2 = 1

i = 2

number = int(input('Введите число: '))
while n2 < number:
    n1, n2 = n2, n2 + n1
    i += 1
if n2 !=number:
    print('-1')
else:
    print(i)


# ------------------------------------------------------------------------------------------------------------------------


# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.


# from random import randint
# len_ght = 30
# i = 1
# otp = 0
# max_otp = 0

# while i <= 30:
#     temp = random.randint(-5,10)
#     print(temp,end = " ")
#     if temp > 0:
#         otp = otp+1

#         if otp > max_otp:
#             max_otp = otp
#     else:
#         otp = 0
#     i = i + 1
# print()
# print("Максимальная длинна оттепели",max_otp)
# print(f'Количество подряд теплых дней:{count}')


# ------------------------------------------------------------------------------------------------------------------------

# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

# import random

# MAX_WEIGHT = 5000
# MIN_WEIGHT = 100


# watermelon = int(input("Введите количество арбузов: "))
# weigth = 0
# max_weigth = MIN_WEIGHT
# min_weigth = MAX_WEIGHT

# for i in range(watermelon):
#     weigth = random.randint(MIN_WEIGHT, MAX_WEIGHT)
#     print(weigth, end=" ")
#     if weigth > max_weigth:
#         max_weigth = weigth
#     elif weigth < min_weigth:
#         min_weigth = weigth
# print(f"\nАрбуз для себя получился на {max_weigth} г, а для тёщи {min_weigth} г. Как-то так")
