from controller import CheckSymbol
from calculator import CalculateElements
from logger import control_logger

P0 = 0

def EnterTheString(update, context):
    is_example_wright = False
    example = update.message.text
    while (is_example_wright == False):
        for i in example:
            if CheckSymbol(i):
                is_example_wright = True
            else:
                is_example_wright == False
                context.bot.send_message(update.effective_chat.id, 'Убедитесь что в выражении только допустимые символы.')
                example = update.message.text
                control_logger(False, update, context)     
                break      
    ShowResult(example, update, context)

def ShowResult(example, update, context):
    context.bot.send_message(update.effective_chat.id, f'Ответ = {CalculateElements(example, update, context)}')


def StartProgram(update, context):
    context.bot.send_message(update.effective_chat.id, f'*** The Calculator ***')
    # print(f"Ответ = {CalculateElements(EnterTheString())}")
    return P0
    
