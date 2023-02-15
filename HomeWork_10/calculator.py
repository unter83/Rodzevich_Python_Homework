import logger

def Operation(example_lst: list, i: int, symbol):
    if symbol == "/":
        result = example_lst[i - 1] / example_lst[i + 1]

    elif symbol == "*":        
        result = example_lst[i - 1] * example_lst[i + 1]

    elif symbol == "-":        
        result = example_lst[i - 1] - example_lst[i + 1]

    elif symbol == "+":        
        result = example_lst[i - 1] + example_lst[i + 1]

    del example_lst[i-1:i+2]

    example_lst.insert(i - 1, result)

    return result

def CalculateElements(example: str, update, context) -> list:
    logger.example_logger(example, update, context)   
    example = example.replace(" ","")

    if example[0] == "-":
        example = "0" + example

    example = example.replace("-"," - ").replace("+", " + ").replace("/"," / ").replace("*", " * ")
    example_lst = list(example.split())

    for i in range(len(example_lst)):

        temp = example_lst[i]
        if temp.replace('.',"").replace(',',"").isdigit():

            if "." in str(example_lst[i]):

                example_lst[i] = float(example_lst[i])
            elif "," in str(example_lst[i]):

                example_lst[i] = float(example_lst[i].replace(',','.'))
            else:

                example_lst[i] = int(example_lst[i])



    operators = ["/", "*", "-", "+"]


    for s in operators:

        i = 0
        while i < len(example_lst):
            if example_lst[i] == s:

                if s == "/":
                    result = Operation(example_lst, i, s)
                    i = 0

                elif s == "*":
                    result = Operation(example_lst, i, s)
                    i = 0

                elif s == "-":
                    result = Operation(example_lst, i, s)
                    i = 0

                elif s == "+":
                    result = Operation(example_lst, i, s)
                    i = 0

            i += 1
    
    logger.result_logger(example, result, update, context)
    return result
