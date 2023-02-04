
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

print(student_dict)  
