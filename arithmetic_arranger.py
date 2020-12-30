import re

def arithmetic_arranger(problems, solution = False):
    # more than five problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
        
    arrangged_problems = ""

    # search each problem for operators adn operands
    for item in problems:
        operator = re.search('[*|/]', item)
        operands = re.split('[+|-]', item)

        if operator:
            return "Error: Operator must be '+' or '-'."
        
        for operand in operands:
            stripOperand = operand.strip()
            nonDigit = re.search('[^0-9]', stripOperand)
            if nonDigit:
                return 'Error: Numbers must only contain digits.'
            
            if len(stripOperand) > 4:
                return 'Error: Numbers cannot be more than four digits.'

    # print top digits
    for item in problems:
        operands = re.split('[+|-]', item)
        first = operands[0].strip()
        second = operands[1].strip()
        sign = re.search('[+|-]', item).group()
        biggest = max([int(first), int(second)])
        dashes = ""
        for i in range(len(str(biggest))+2):
            dashes += "-"

        sol = "{}    "

        arrangged_problems += sol.format(first.rjust(len(str(biggest))+2))

    # line break
    arrangged_problems += "\n"

    # print bottom digits
    for item in problems:
        operands = re.split('[+|-]', item)
        first = operands[0].strip()
        second = operands[1].strip()
        sign = re.search('[+|-]', item).group()
        biggest = max([int(first), int(second)])
        dashes = ""
        for i in range(len(str(biggest))+2):
            dashes += "-"

        sol = "{} {}    "

        arrangged_problems += sol.format(sign, second.rjust(len(str(biggest))))

     # line break
    arrangged_problems += "\n"

    # print dashes
    for item in problems:
        operands = re.split('[+|-]', item)
        first = operands[0].strip()
        second = operands[1].strip()
        sign = re.search('[+|-]', item).group()
        biggest = max([int(first), int(second)])
        dashes = ""
        for i in range(len(str(biggest))+2):
            dashes += "-"

        sol = "{}    "

        arrangged_problems += sol.format(dashes)
        
    return arrangged_problems
#     # return test

test = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
arithmetic_arranger(test)