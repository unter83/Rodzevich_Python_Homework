from datetime import datetime as dt

def example_logger(example, update, context):
    time = dt.now().strftime('%m/%d/%Y %H:%M:%S')
    with open('HomeWork_10/log.txt', 'a') as file:
        file.write("{} - {} entered {}\n".format(time, str(update.message.from_user.username), example))

def result_logger(example, result, update, context):
    time = dt.now().strftime('%m/%d/%Y %H:%M:%S')
    with open('HomeWork_10/log.txt', 'a') as file:
        file.write("{} - result is {} for example {}\n".format(time, result, example))

def control_logger(control, update, context):
    time = dt.now().strftime('%m/%d/%Y %H:%M:%S')
    if not control:
        with open('HomeWork_10/log.txt', 'a') as file:
            file.write("{} - {} entered invalid example\n".format(time, str(update.message.from_user.username)))