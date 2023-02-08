def Remove(msg):
    msg = msg[7:len(msg)]
    work_msg = ''
    rem_msg = ''    
    count = 0
    for i in msg:
        count += 1        
        if i == '"':
            break
        rem_msg += i
    msg = msg[count:len(msg)]
    rem_msg = rem_msg.replace(' ', '')
    quote = True
    for i in msg:        
        if i == '"' and quote == True:
            quote = False
            is_quote = True
            break
        work_msg = work_msg + i
    print(rem_msg)
    print(msg)
    print(work_msg)

    rep_msg = work_msg.replace(rem_msg, "")
    print(rep_msg)

update = input()
Remove(update)