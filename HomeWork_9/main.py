from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from bot_commands import Start, Remove
import game

bot = Bot(token='5862603097:AAG6kCvFbxV4b11DDytzpB5DVVES-bosaLo')
updater = Updater(token='5862603097:AAG6kCvFbxV4b11DDytzpB5DVVES-bosaLo')

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', Start)
remove_handler = CommandHandler('remove', Remove)
start_game_handler = CommandHandler('game', game.StartGame)
user1_hander = MessageHandler(Filters.text, game.Player1_Takes_Candy)
error_handler = CommandHandler('error', game.Error)
game_handler = ConversationHandler(entry_points=[start_game_handler], states={game.P0: [user1_hander], game.P1: [user1_hander], game.P2: [user1_hander], game.P3: [user1_hander]}, fallbacks=[error_handler])



dispatcher.add_handler(start_handler)
dispatcher.add_handler(remove_handler)
dispatcher.add_handler(start_game_handler)
dispatcher.add_handler(user1_hander)
dispatcher.add_handler(game_handler)






print('Server start')
updater.start_polling()
updater.idle()