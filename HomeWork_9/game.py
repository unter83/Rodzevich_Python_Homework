from telegram.ext import  ConversationHandler
import random

max_candy = 28
max_candy_pool = 120

P0 = 0
P1 = 1
P2 = 2
P3 = 3
P4 = 4

candy_pool = max_candy_pool 
player1_candy = 0
player_bot_candy = 0
candy_taken = 0


def Player1_Takes_Candy(update, context):
    candy_taken = update.message.text  
    global candy_pool, rounds_left
    if candy_taken.isdigit():
        candy_taken = int(candy_taken)
        if (candy_taken > 0 and candy_taken <= max_candy):
            if candy_pool >= candy_taken:
                context.bot.send_message(update.effective_chat.id, f"Игрок берёт {candy_taken} конфет")
                candy_pool = candy_pool - candy_taken
                context.bot.send_message(update.effective_chat.id, f"На столе осталось {candy_pool} конфет")
                if candy_pool <= 0:
                    context.bot.send_message(update.effective_chat.id, f"Победил игрок")
                    return ConversationHandler.END
                Bot_Takes_Candy(update, context)                
                return P1
            else:
                candy_taken = candy_pool                
                candy_pool = 0
                context.bot.send_message(update.effective_chat.id, f"Игрок берёт {candy_taken} конфет. На столе осталось {candy_pool} конфет")
                if candy_pool <= 0:
                    context.bot.send_message(update.effective_chat.id, f"Победил игрок")
                    return ConversationHandler.END 
                Bot_Takes_Candy(update, context) 
                return P1  
        else:
            context.bot.send_message(update.effective_chat.id, f"Вы можете взять от 1 до {max_candy} конфет")
            return P2
    else:
        context.bot.send_message(update.effective_chat.id, "Введите число")
        return P3

   

def Bot_Takes_Candy(update, context):
    
    global candy_pool
    candy_taken = random.randint(1,29)
    if candy_pool >= candy_taken:
        candy_pool -= candy_taken
        context.bot.send_message(update.effective_chat.id, f"Компьютер берёт {candy_taken} конфет. На столе осталось {candy_pool} конфет")
        if candy_pool <= 0:
            context.bot.send_message(update.effective_chat.id, f"Победил компьютер")
            return ConversationHandler.END   
    else:
        candy_taken = candy_pool
        candy_pool -= candy_taken
        context.bot.send_message(update.effective_chat.id, f"Компьютер берёт {candy_taken} конфет. На столе осталось {candy_pool} конфет")
        if candy_pool <= 0:
            context.bot.send_message(update.effective_chat.id, f"Победил компьютер")
            return ConversationHandler.END

def StartGame(update, context):
    context.bot.send_message(update.effective_chat.id, f'*** Игра в конфеты  ***\n')
    context.bot.send_message(update.effective_chat.id, f"На столе лежит {max_candy_pool} конфет. Играют два игрока делая ход друг после друга.\nПервый ход делает человек. За один ход можно забрать не более чем {max_candy} конфет.\n")
    return P0


def Error(update, context):
    context.bot.send_message(update.effective_chat.id, f'Что-то пошло не так')

