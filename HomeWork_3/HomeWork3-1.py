import random

def CreateRandomArray(list_limit, min, max: int) -> list: 
    list_of_num = []
    for i in range(0, list_limit):
        list_of_num.append(random.randint(min, max))
    return list_of_num

print("Программа находит сумму элементов списка, стоящих на нечётной позиции.\n")

list_limit = int(input("Введите длину списка случайных чисел: "))
min = int(input("Введите минимальное число: "))
max = int(input("Введите максимальное число: "))

list_of_num = CreateRandomArray(list_limit, min, max)
print(list_of_num)
print()
sum = 0
for i in range(0, list_limit):
    if (i % 2):
        print(list_of_num[i], end =" ")
        sum += list_of_num[i]
print()
print(f"Сумма элементов на нечётны позициях {sum}")