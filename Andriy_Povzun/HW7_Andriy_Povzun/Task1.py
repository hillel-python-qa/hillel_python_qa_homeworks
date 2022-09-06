def calculator(first_operand, second_operand, action):
    if action == "+":
        result = first_operand + second_operand
        return result
    elif action == '-':
        result = first_operand - second_operand
        return result
    elif action == '*':
        result = first_operand * second_operand
        return result
    elif action == '/':
        result = first_operand / second_operand
        return result
    else:
        raise Exception(f'Not known operation: {action}. Must be "+", "-", "*", "/"')
