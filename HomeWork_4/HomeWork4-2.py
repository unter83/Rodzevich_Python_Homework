print("Программа выводит список простых множителей для заданного числа\n")

num = int(input("Введите число: "))
t_num = num
print(f"{num} = ", end ="")
count = False
i = 1
while i <= t_num:
# for i in range(2, t_num+1):
    i = i + 1
    if (t_num % i == 0) and (count == False):
        t_num = int(t_num / i)
        print(f"{i}", end="")       
        i = 1
        count = True        
    elif (t_num % i == 0) and (count == True):
        t_num = int(t_num / i)
        print(f" * {i}", end="")
        i = 1
    if t_num == 1:
        break
    if i > t_num:
        print(f" * {t_num}")
        break
    