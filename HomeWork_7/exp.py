
def ExportContact(data):
    s_name, f_name, tel, comment = data
    contact = s_name + '\n' + f_name + '\n' + tel + '\n' + comment + '\n' + '-----------\n'
    path = 'HomeWork_7/tel.txt'
    print(f"\nДобавление контакта в фаил {path}")
    with open(path, 'a') as file:
        file.write(contact)
    return True

def ExportContact2(data):
    
    s_name, f_name, tel, comment = data
    contact = s_name + ',' + f_name + ',' + tel + ',' + comment + '\n'
    path = 'HomeWork_7/contacts.txt'
    print(f"\nДобавление контакта в фаил {path}")
    with open(path, 'a') as file:
        file.write(contact)
    return True
