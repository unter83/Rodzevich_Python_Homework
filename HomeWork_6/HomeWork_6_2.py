print("Программа делит список на 2 списка состоящих из чисел и строк\n")

lst = list(map(str, input("Введите сторки, разделяя их проблеми: ").split()))
lst_2 = [0]*2

lst_2[0]= list(filter(lambda i: i.isdigit(), lst))
lst_2[1]= list(filter(lambda i: not i.isdigit(), lst))
print(lst_2)