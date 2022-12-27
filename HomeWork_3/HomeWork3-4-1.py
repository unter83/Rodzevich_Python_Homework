print("Программа преобразует десятичное число в двоичное методом рекурсии\n")

def Binary(div):
    if div != 0:   
        Binary(div // 2)
        print(div % 2, end = "")

num = int(input("Введите число: "))
print("\nЧисло в двоичном виде:", end =" ")
Binary(num)