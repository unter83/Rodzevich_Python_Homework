def GetSudents():
    s_path='HomeWork_8/students_db.txt'
    with open(s_path,'r', encoding='utf8') as file:
        student_str = file.read()

    student_dict = {}
    key_count = student_str.count('s_key=')
    # print(key_count)
    k = 0
    pos = 0

    while(k < key_count):
        key = ''
        student_name = ''
        student_secname = ''
        pos = student_str.index('s_key=', pos) + 6
        while (student_str[pos] != ';'):
            key = key + student_str[pos]
            pos += 1
            # print(key)
        # print(f'key = {key}')
        
        pos += 1
        pos = student_str.index('s_name=', pos) + 7
        while (student_str[pos] != ';'):
            student_name = student_name + student_str[pos]
            pos += 1
            # print(lesson)
        # print(f'student_name = {student_name}')

        pos += 1
        pos = student_str.index('s_secname=', pos) + 10
        while (student_str[pos] != ';'):
            student_secname = student_secname + student_str[pos]
            pos += 1
            # print(lesson)
        # print(f'student_secname = {student_secname}')   

        student_dict[int(key)] = student_name + ' ' + student_secname
        k += 1
    return student_dict
    # print(student_dict)  

def ShowAllStudents():
    student_dict = GetSudents()
    path = 'HomeWork_8/students_db.txt'
    with open(path,'r', encoding='utf8') as file:
        data = file.read()
    data = data.replace('s_key=', '').replace(';s_name=', ' - ').replace(';s_secname=', ' ').replace(';', '')    
    print(data)
    return student_dict


def ShowStudent(student):
    student_dict = GetSudents()
    # print(student_dict[student])
    path = 'HomeWork_8/Students/' + str(student) + '.txt'
    # with open(path,'r', encoding='utf8') as file:
    #     data = file.read()
    #     print(data)
    try:
        file = open(path,'r', encoding='utf8')           
        data = file.read()
        print(data)
        file.close()
    except:
        file = open(path,'a', encoding='utf8')        
        file.close()

    


def FindStudent(f_name, s_name):
    students_dict = GetSudents()
    name = f_name + " " + s_name
    if name in students_dict.values():
        key = 0
        while students_dict[key] != name:
            key += 1
        std_data = (key, students_dict[key])
        return std_data
    else:        
        return 'Not_found'