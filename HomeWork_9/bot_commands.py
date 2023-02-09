from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5862603097:AAG6kCvFbxV4b11DDytzpB5DVVES-bosaLo')
updater = Updater(token='5862603097:AAG6kCvFbxV4b11DDytzpB5DVVES-bosaLo')

dispatcher = updater.dispatcher

def Start(update, context):
    name = str(update.message.from_user.username)
    welcom_msg = f'Привет {name}. \n\
    Чтобы запустить программу по удалению строки в фразе введите команду\
    /remove, затем, которую хотите удалить, затем в ковычках сообщение\
    из которого надо удалить строку.\n\
    Например: /remove бот "Я не робот"'
    context.bot.send_message(update.effective_chat.id, welcom_msg)

def Remove(update, context):
    # msg = input("_")
    msg = update.message.text
    is_quote = False
    msg = msg[7:len(msg)]
    new_msg = ''
    str_to_remove = ''    
    count = 0
    for i in msg:
        count += 1        
        if i == '"':
            is_quote = True
            break
        str_to_remove += i
    msg = msg[count:len(msg)]
    str_to_remove = str_to_remove.replace(' ', '')
    list_msg = list(msg.split())
    for i in list_msg:        
        if str_to_remove in i:
            list_msg.remove(i)
    print(list_msg)
    for i in list_msg:
       new_msg += str(i) + " "
    print(new_msg)
    if is_quote == False:
        new_msg = 'Проверьте правильность команды'
    context.bot.send_message(update.effective_chat.id, str(new_msg))

# Remove(1,2)
# start_handler = CommandHandler('start', Start)
# remove_handler = CommandHandler('remove', Remove)


# dispatcher.add_handler(start_handler)
# dispatcher.add_handler(remove_handler)


# print('Server start')
# updater.start_polling()
# updater.idle()