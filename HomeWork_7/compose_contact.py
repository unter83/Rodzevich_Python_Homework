import csv

def ComposeContact(s_name, f_name, tel, comment):
    print("Составление контакта")
    

    data = s_name + '\n' + f_name + '\n' + tel + '\n' + comment + '\n' + '-----------'
    return  