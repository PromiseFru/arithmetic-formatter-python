import re

def arithmetic_arranger(problems, solution = False):
    # search each probelm for operators
    for item in problems:
        operator = re.search('[*|/]', item)
        if operator:
            print("Error: Operator must be '+' or '-'") 
            return

    # more than five problems
    if len(problems) > 5:
        print('Error: Too many problems') 
        return

    for item in problems:
        operands = re.split('\+|\-', item)
        print(operands)
    # return arranged_problems

test = ["32 + 698", "3801 - 2", "45 * 43", "123 + 49"]
arithmetic_arranger(test)