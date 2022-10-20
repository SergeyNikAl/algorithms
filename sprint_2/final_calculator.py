# ID: 71289624
import operator

ARITHMETIC_FUNCTIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


class Stack:

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            raise IndexError('Стек пуст. Нельзя удалить значения.')


def calculate(
        operands, stack=None, value_type=int, operators=ARITHMETIC_FUNCTIONS
):
    stack = Stack() if stack is None else stack
    for value in operands:
        if value in operators:
            operand_1, operand_2 = stack.pop(), stack.pop()
            stack.push(operators[value](operand_2, operand_1))
        else:
            try:
                stack.push(value_type(value))
            except ValueError:
                raise ValueError(f'Невозможно преобразовать значение {value}')
    return stack.pop()


if __name__ == '__main__':
    print(calculate(input().split()))
