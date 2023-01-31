import csv

def ComposeContact(s_name, f_name, tel, comment):
    print("Экспорт контакта")

    data = s_name + '\n' + f_name + '\n' + tel + '\n' + comment + '\n' + '-----------'
    
    with open('tel.txt', 'a') as file:
        file.write(data1)