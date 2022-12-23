print("Программа находит произведение чисел, которые указываются в виде индексов, из последовательности -N, N \n")

num = int(input("Введите число N: "))

li = list(range(-num, num + 1))

print(li)

print("Введите индексы массива, разделяя их пробелом. У первого элемента массива индекс 1.")
indexes = input().split()
int_indexes = list(map(int, indexes))

print(int_indexes)
prod = 1
for i in int_indexes:
    if i > (2 * num + 1) or i <= 0:
        print("Укажите индкесы в допустимом диаазоне")
        exit()
    print(li[i - 1])
    prod = prod * li[i - 1]

print (f"Произвдение чисел {prod}")

