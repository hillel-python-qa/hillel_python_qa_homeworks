def calculator(first_operand: int, second_operand: int, action: str):
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
