def GetLessons():
    l_path='HomeWork_8/lessons_db.txt'
    with open(l_path,'r', encoding='utf8') as file:
        lesson_str = file.read()

    lesson_dict = {}
    key_count = lesson_str.count('l_key=')
    # print(key_count)
    k = 0
    pos = 0

    while(k < key_count):
        key = ''
        lesson = ''
        pos = lesson_str.index('l_key=', pos) + 6
        while (lesson_str[pos] != ';'):
            key = key + lesson_str[pos]
            pos += 1
            # print(key)
        # print(f'key = {key}')
        
        pos += 1
        pos = lesson_str.index('l_name=', pos) + 7
        while (lesson_str[pos] != ';'):
            lesson = lesson + lesson_str[pos]
            pos += 1
            # print(lesson)
        # print(f'lesson = {lesson}')
        lesson_dict[int(key)] = lesson
        k += 1
    return lesson_dict
    # print(lesson_dict)  

def ShowLessons():
    lessons_dict = GetLessons()
    # print(student_dict[student])
    path = 'HomeWork_8/lessons_db.txt'
    with open(path,'r', encoding='utf8') as file:
        data = file.read()
    data = data.replace('l_key=', '').replace(';l_name=', ' - ').replace(';', '')

    print(data)
    return lessons_dict