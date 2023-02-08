from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random

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
    msg = update.message.text
    msg = msg[7:len(msg)]
    work_msg = ''
    str_to_remove = ''    
    count = 0
    is_quote = False
    for i in msg:
        count += 1        
        if i == '"':
            break
        str_to_remove += i
    msg = msg[count:len(msg)]
    str_to_remove = str_to_remove.replace(' ', '')
    quote = True
    for i in msg:        
        if i == '"' and quote == True:
            quote = False
            is_quote = True
            break
        work_msg = work_msg + i
    new_msg = work_msg.replace(str_to_remove, "")

    
    if is_quote == False:
        work_msg = 'Проверьте правильность команды'
    context.bot.send_message(update.effective_chat.id, new_msg)

start_handler = CommandHandler('start', Start)
remove_handler = CommandHandler('remove', Remove)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(remove_handler)

print('Server start')
updater.start_polling()
updater.idle()