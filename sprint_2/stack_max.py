class StackMax:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            self.items.pop()
        return 'error'

    def get_max(self):
        if self.items:
            return max(self.items)
        return None


if __name__ == '__main__':
    stack = StackMax()
    commands = [input().split() for _ in range(int(input()))]
    for command in commands:
        if command[0] == 'push':
            stack.push(command[1])
        if command[0] == 'pop':
            print(stack.pop())
        else:
            print(stack.get_max)
