print("Программа оставляет в списке только двузначные числа\n")

lst = list(map(int, input("Введите числа, разделяя их проблеми: ").split()))
lst_2 = [i for i in lst if 100 > i > 9]
lst_3 = list(filter(lambda i: 100 > i > 9, lst))
print(lst_2)
print(lst_3)


