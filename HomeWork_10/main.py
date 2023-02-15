from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

import user_interface as ui

P0 = 1

bot = Bot(token='5862603097:AAG6kCvFbxV4b11DDytzpB5DVVES-bosaLo')
updater = Updater(token='5862603097:AAG6kCvFbxV4b11DDytzpB5DVVES-bosaLo')

dispatcher = updater.dispatcher

def Error(update, context):
    context.bot.send_message(update.effective_chat.id, 'Какая-то ошибка!')


# if __name__ == '__main__':
#     main()

start_handler = CommandHandler('start', ui.StartProgram)
calculate_handler = MessageHandler(Filters.text, ui.EnterTheString)
error_handler = CommandHandler('error', Error)
result_handler = ConversationHandler(entry_points=[start_handler], states={ui.P0: [calculate_handler]}, fallbacks=[error_handler])

# dispatcher.add_handler(start_handler)
dispatcher.add_handler(result_handler)

print('Server start')
updater.start_polling()
updater.idle()