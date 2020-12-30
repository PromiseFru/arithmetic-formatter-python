import re

def arithmetic_arranger(problems, solution = False):
    # more than five problems
    if len(problems) > 5:
        print('Error: Too many problems.') 
        return
        
    # search each problem for operators
    for item in problems:
        operator = re.search('[*|/]', item)
        operands = re.split('[+|-]', item)

        if operator:
            print("Error: Operator must be '+' or '-'.") 
            return
        
        for operand in operands:
            stripOperand = operand.strip()
            nonDigit = re.search('[^0-9]', stripOperand)
            if nonDigit:
                print('Error: Numbers must only contain digits.')
                return
            
            if len(stripOperand) > 4:
                print('Error: Numbers cannot be more than four digits.')
                return

    # return arranged_problems

# test = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
# arithmetic_arranger(test)