import math

def math_thing(expression):
    expression = expression.replace(' ', '')
    symbols = ['+', '-', '*', '/']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    indexes = []
    placeholder = [0]
    re = []

    if expression.count('(') > expression.count(')'):
        indexes.append(expression.index('('))
        placeholder.append(expression.index(']'))
        for i in range(max(indexes) + 3, max(placeholder)):
            if expression[i] in numbers and expression[i + 1] not in numbers:
                re.append(i + 2)
        
        

    elif expression.count('(') < expression.count(')'):
        indexes.append(expression.index(')'))
        if expression.count('[') != 0:
            placeholder.append(expression.index('['))
        else:
            re.append(1)
        for i in range(max(placeholder), min(indexes)):
            if expression[i] not in symbols and expression[i - 1] not in numbers:
                re.append(i - 1)
        if expression.count('[') != 0:
            re.remove(re[0])


    elif expression.count('[') > expression.count(']'):
        indexes.append(expression.index('['))
        placeholder.append(expression.index(')'))
        for i in range(max(placeholder), len(expression)):
            if i == len(expression) - 1:
                re.append(i + 2)
    
        for i in range(max(placeholder), len(expression) - 1):
            if expression[i - 1] == ')' :
                re.append(i + 1)
            if expression[i] in numbers and expression[i + 1] not in numbers:
                re.append(i + 2)
        

    elif expression.count('[') < expression.count(']'):
        indexes.append(expression.index(']'))
        placeholder.append(expression.index('('))
        for i in range(1, max(placeholder) + 2):
            if expression[i - 1] == '(':
                re.append(i)
            elif expression[i] in numbers and expression[i - 1] not in numbers:
                re.append(i + 1)
        re.append(1)

        
    re = list(set(re))
    return re
    

    

# print(math_thing('[2+3*8-3)]+6'))
# print(math_thing('[(5+5-2]*5'))
# print(math_thing('[4/(12-8/4*25]'))
# print(math_thing('[(2-5)+6'))
# print(math_thing('13-[(6+18)/3*22'))
# print(math_thing('12+[10/(2-3]*8'))
# print(math_thing('45/5/(3+2)*3]*5'))
# print(math_thing('1+[2-(3*4/5]*6'))
print(math_thing('32/4)*2'))