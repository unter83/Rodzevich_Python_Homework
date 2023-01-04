print("Программа удаляет из строки чисел все повторы\n")

numbers = input("Введите последовательность чисел через пробел: ").split()
list_of_num = list(map(int, numbers))
print()

list_of_dubs = []
j = 0
for i in list_of_num:
    j = list_of_num.index(i) + 1
    while j < len(list_of_num):
        if i == list_of_num[j]:
            if i not in list_of_dubs:
                list_of_dubs.append(i)
            break
        j += 1

list_of_not_dubs = []

for i in list_of_num:
    if i not in list_of_dubs:
        list_of_not_dubs.append(i)

print("Список чисел повторяющихся в искомой последовательности: ", end=" ")
print(list_of_dubs)

print("Список чисел не повторяющихся в искомой последовательности: ", end=" ")
print(list_of_not_dubs)