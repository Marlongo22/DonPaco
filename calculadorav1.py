
def sum(a, b):
    return a+b

def subtraction(a, b):
    return a-b

def product(a, b):
    return a*b

def division(a, b):
    return a/b

def exponent(base, exponent):
    number = base
    counter = 1
    while counter<exponent:
        number = number*base
        counter += 1
    return number

print('\n Digite su problema combinando las operaciones si necesario, sin usar parentesis')
print('''
    Suma: +
    Resta: -
    Multiplicion: *
    Division: /
    Potencia: ^
    Salir: Q
''')

while True:
    user_operation = input('> ')
    if user_operation=='Q' or user_operation=='q':
        break

    "NUMBERS AND OPERATORS SEPARATION"

    operators_delimeters = "^/*-+"
    new_delimiter = '|'

    # creates a list with the operators in order
    operation_operators = []
    for delimeter in user_operation:
        if delimeter in operators_delimeters:
            operation_operators += delimeter        

    # replace each delimiter with the new delimiter character (this is for creating the numbers list)
    user_operation_modified = user_operation
    for character in user_operation:
        if character in operators_delimeters:
            user_operation_modified = user_operation_modified.replace(character, new_delimiter)
    # creates a list with the numbers(using the user_operation_modified string)
    numbers = user_operation_modified.split(new_delimiter)
    numbers = [int(x) for x in numbers] # transfors the numbers string list into an integer list


    number0 = numbers[0]
    number1 = numbers[1]

    # print('data:')
    # print(numbers)
    # print(operation_operators)
    # print('\n')

    # solves the exponents and (a^b) replacing them with c
    for operator in operation_operators:
        if operator=='^':
            opr_index = operation_operators.index(operator)
            exp_result = exponent(numbers[opr_index], numbers[opr_index+1])
            operation_operators.pop(opr_index)
            numbers.pop(opr_index)
            numbers.pop(opr_index)
            numbers.insert(opr_index, exp_result)

    for operator in operation_operators:
        if operator=='*':
            opr_index = operation_operators.index(operator)
            exp_result = product(numbers[opr_index], numbers[opr_index+1])
            operation_operators.pop(opr_index)
            numbers.pop(opr_index)
            numbers.pop(opr_index)
            numbers.insert(opr_index, exp_result)
    
    for operator in operation_operators:
        if operator=='/':
            opr_index = operation_operators.index(operator)
            exp_result = division(numbers[opr_index], numbers[opr_index+1])
            operation_operators.pop(opr_index)
            numbers.pop(opr_index)
            numbers.pop(opr_index)
            numbers.insert(opr_index, exp_result)
    
    for operator in operation_operators:
        if operator=='+':
            opr_index = operation_operators.index(operator)
            exp_result = sum(numbers[opr_index], numbers[opr_index+1])
            operation_operators.pop(opr_index)
            numbers.pop(opr_index)
            numbers.pop(opr_index)
            numbers.insert(opr_index, exp_result)

    for operator in operation_operators:
        if operator=='-':
            opr_index = operation_operators.index(operator)
            exp_result = subtraction(numbers[opr_index], numbers[opr_index+1])
            operation_operators.pop(opr_index)
            numbers.pop(opr_index)
            numbers.pop(opr_index)
            numbers.insert(opr_index, exp_result)

    # print(numbers)
    # print(operation_operators, '\n')
    print('result: ', numbers[0])
