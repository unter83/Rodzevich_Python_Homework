import random

print("Программа формирует случайный многочлен степени K\n")

num = int(input("Введите степень многочлена: "))
i = num
start = False
r = 101
while i >= 0:

    if i > 1 and start == False:
        k = random.randint(0, r)
        
        if k > 1:        
            print(f"{k}*x^{i}", end="")
            start = True
        elif k == 1:
            print(f"x^{i}", end="")
            start = True

    elif i == 1 and start == False:
        k = random.randint(0, r)
        
        if k > 1:       
            print(f"{k}*x" , end="")
            start = True
        elif k == 1:
            print(f"x" , end="")
            start = True

    elif i == 0 and start == False:
        k = random.randint(0, r)
        
        if k > 1:       
            print(f"{k}" , end="")
            start = True
    
    if i > 1 and start == True:
        k = random.randint(0, r)
        if k > 1:        
            print(f" + {k}*x^{i}", end="")
        elif k == 1:
            print(f" + x^{i}", end="")
    elif i == 1:
        k = random.randint(0, r)
        if k > 1:       
            print(f" + {k}*x" , end="")
        elif k == 1:
            print(f" + x" , end="")
    elif i == 0:
        k = random.randint(0, r)
        if k >= 1:       
            print(f" + {k}" , end="")

    i -= 1