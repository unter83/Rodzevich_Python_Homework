import random

def CreateRandomArray(list_limit, min, max: int) -> list: 
    list_of_num = []
    for i in range(0, list_limit):
        list_of_num.append(random.randint(min, max))
    return list_of_num

print("Программа которая находит произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.\n")

list_limit = int(input("Введите длину списка случайных чисел: "))
min = int(input("Введите минимальное число случайной последовательности: "))
max = int(input("Введите максимальное число случайной последовательности: "))

list_of_num = CreateRandomArray(list_limit, min, max)
print(list_of_num)
print()

print("Произведение пар:")
for i in range(0, list_limit // 2 + 1):
    # k = list_limit - i
    # print(i)
    print(f"{list_of_num[i]} * {list_of_num[list_limit - i - 1]} = {list_of_num[i]*list_of_num[list_limit - i - 1]}")
