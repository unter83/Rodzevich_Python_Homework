import math

def Polinom(file: str) -> dict:
    data = open(file, "r")
    print(type(data))
    poly = data.read()
    data.close()
    print(poly)
    poly_res = poly.replace(" ", "")
    poly_res = poly_res.replace("*", "")
    poly_res = poly_res.replace("+", " +")
    poly_res = poly_res.replace("-", " -")
    
    poly_res_array = poly_res.split(" ")
    polinom_dict = {}

    print(poly_res_array)

    for i in poly_res_array:
        if "x" not in i:
            index = "0"            
            value = i
            print(f"{float(value)} - значение")
            print(f"{int(index)} - индекс")
            polinom_dict[int(index)] = float(value)
        else:
            value = ""
            t = 0
            while i[t] != "x":
                value = value + i[t]
                t += 1
            print(f"{float(value)} - значение")

            index = ""
            while t < len(i):
                index = index + i[t]
                t += 1
            index = index.replace("^", "")
            index = index.replace("x", "")
            if index == "":
                index = "1"
            print(f"{int(index)} - индекс")
            polinom_dict[int(index)] = float(value)


    print(polinom_dict)
    print("---------------")
    return(polinom_dict)


print("Программа читает из двух файлов многочлены и создаёт новый фаил с суммой многочленов\n")

p1 = Polinom("HomeWork_4/1.txt")
p2 = Polinom("HomeWork_4/2.txt")
p_res = {}

for i in p1:
    if i in p2:
       p_res[i] = p1.get(i) + p2.get(i)
    else:
        p_res[i] = p1.get(i)
    
for i in p2:
    if i in p1:
        p_res[i] = p1.get(i) + p2.get(i)
    else:
        p_res[i] = p2.get(i)

print(f"Словарь - {p_res}")
p_res = dict(sorted(p_res.items(), reverse=True))

for i in p_res:
    if float(p_res[i]).is_integer():
        p_res[i] = int(p_res[i])


first = True
result = ""

for i in p_res:
    if first == True:
        if i > 1:
            if p_res[i] > 1 or (0 < p_res[i] < 1):
                result += f"{abs(p_res[i])}*x^{i} "
                print(f"{abs(p_res[i])}*x^{i} ", end="")
                first = False
            elif p_res[i] == 1:
                result += f"x^{i} "
                print(f"x^{i} ", end="")
                first = False
            elif p_res[i] == -1:
                result += f"- x^{i} "
                print(f"- x^{i} ", end="")
                first = False
            elif p_res[i] < 0 or (-1 < p_res[i] < 0):
                result += f"- {abs(p_res[i])}*x^{i} "
                print(f"- {abs(p_res[i])}*x^{i} ", end="")
                first = False
        elif i == 1:
            if p_res[i] > 1 or (0 < p_res[i] < 1):
                result += f"{abs(p_res[i])}*x "
                print(f"{abs(p_res[i])}*x ", end="")
                first = False
            elif p_res[i] == 1:
                result += f"x "
                print(f"x ", end="")
                first = False
            elif p_res[i] == -1:
                result += f"- x "
                print(f"- x ", end="")
                first = False
            elif p_res[i] < 0 or (-1 < p_res[i] < 0):
                result += f"- {abs(p_res[i])}*x "
                print(f"- {abs(p_res[i])}*x ", end="")
                first = False
             
    else:
        if i > 1:
            if p_res[i] > 1 or (0 < p_res[i] < 1):
                result += f"+ {abs(p_res[i])}*x^{i} "
                print(f"+ {abs(p_res[i])}*x^{i} ", end="")

            elif p_res[i] == 1:
                result += f"+ x^{i} "
                print(f"+ x^{i} ", end="")

            elif p_res[i] == -1:
                result += f"- x^{i} "
                print(f"- x^{i} ", end="")

            elif p_res[i] < 0 or (-1 < p_res[i] < 0):
                result += f"- {abs(p_res[i])}*x^{i} "
                print(f"- {abs(p_res[i])}*x^{i} ", end="")

        elif i == 1:
            if p_res[i] > 1 or (0 < p_res[i] < 1):
                result += f"+ {abs(p_res[i])}*x "
                print(f"+ {abs(p_res[i])}*x ", end="")

            elif p_res[i] == 1:
                result += f"+ x "
                print(f"+ x ", end="")

            elif p_res[i] == -1:
                result += f"- x "
                print(f"- x ", end="")

            elif p_res[i] < 0 or (-1 < p_res[i] < 0):
                result += f"- {abs(p_res[i])}*x "
                print(f"- {abs(p_res[i])}*x ", end="")

        elif i == 0:
            if p_res[i] > 1 or (0 < p_res[i] < 1):
                result += f"+ {abs(p_res[i])} "
                print(f"+ {abs(p_res[i])} ", end="")

            elif p_res[i] == 1:
                result += f"+ "
                print(f"+ ", end="")

            elif p_res[i] == -1:
                result += f"- "
                print(f"- ", end="")

            elif p_res[i] < 0 or (-1 < p_res[i] < 0):
                result += f"- {abs(p_res[i])} "
                print(f"- {abs(p_res[i])} ", end="")
print ()
print (result)

file = open("HomeWork_4/result.txt", "w")
file.write(result)
file.close()

# for i in p_res:
#     if first == True:
#         if i > 1:
#             if p_res[i] > 1 or (0 < p_res[i] < 1):
#                 print(f"{abs(p_res[i])}*x^{i} ", end="")
#                 first = False
#             elif p_res[i] == 1:
#                 print(f"x^{i} ", end="")
#                 first = False
#             elif p_res[i] == -1:
#                 print(f"- x^{i} ", end="")
#                 first = False
#             elif p_res[i] < 0 or (-1 < p_res[i] < 0):
#                 print(f"- {abs(p_res[i])}*x^{i} ", end="")
#                 first = False
#         elif i == 1:
#             if p_res[i] > 1 or (0 < p_res[i] < 1):
#                 print(f"{abs(p_res[i])}*x ", end="")
#                 first = False
#             elif p_res[i] == 1:
#                 print(f"x ", end="")
#                 first = False
#             elif p_res[i] == -1:
#                 print(f"- x ", end="")
#                 first = False
#             elif p_res[i] < 0 or (-1 < p_res[i] < 0):
#                 print(f"- {abs(p_res[i])}*x ", end="")
#                 first = False
             
#     else:
#         if i > 1:
#             if p_res[i] > 1 or (0 < p_res[i] < 1):
#                 print(f"+ {abs(p_res[i])}*x^{i} ", end="")

#             elif p_res[i] == 1:
#                 print(f"+ x^{i} ", end="")

#             elif p_res[i] == -1:
#                 print(f"- x^{i} ", end="")

#             elif p_res[i] < 0 or (-1 < p_res[i] < 0):
#                 print(f"- {abs(p_res[i])}*x^{i} ", end="")

#         elif i == 1:
#             if p_res[i] > 1 or (0 < p_res[i] < 1):
#                 print(f"+ {abs(p_res[i])}*x ", end="")

#             elif p_res[i] == 1:
#                 print(f"+ x ", end="")

#             elif p_res[i] == -1:
#                 print(f"- x ", end="")

#             elif p_res[i] < 0 or (-1 < p_res[i] < 0):
#                 print(f"- {abs(p_res[i])}*x ", end="")

#         elif i == 0:
#             if p_res[i] > 1 or (0 < p_res[i] < 1):
#                 print(f"+ {abs(p_res[i])} ", end="")

#             elif p_res[i] == 1:
#                 print(f"+ ", end="")

#             elif p_res[i] == -1:
#                 print(f"- ", end="")

#             elif p_res[i] < 0 or (-1 < p_res[i] < 0):
#                 print(f"- {abs(p_res[i])} ", end="")
            


