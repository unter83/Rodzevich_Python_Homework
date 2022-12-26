import random, math

def CreateRandomFloatArray(list_limit, min, max: int) -> list: 
    list_of_num = []
    for i in range(0, list_limit):
        list_of_num.append(round(random.random() + random.randint(min, max), 2))
    return list_of_num 
# random.randint(min, max) + 
print("Программа которая найдёт разницу между максимальным и минимальным значением дробной части элементов списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.\n")

list_limit = int(input("Введите длину списка случайных чисел: "))
min = int(input("Введите минимальное число случайной последовательности: "))
max = int(input("Введите максимальное число случайной последовательности: "))

list_of_num = CreateRandomFloatArray(list_limit, min, max)
print(list_of_num)
print()

min = list_of_num[0]
max = list_of_num[0]
for i in list_of_num:
    if (i > max):
        max = i
    if (i < min):
        min = i

print()
print(f"Минимальный элемент - {min}, максимальный элемент - {max}")

print()

print(f"Разница между значениями дробной части - {round(abs((max - min) - round(max - min)), 2)}")