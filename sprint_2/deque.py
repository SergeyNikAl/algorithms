class MyQueueSized:

    def __init__(self, max_s):
        self.queue = [None] * max_s
        self.max_size = max_s
        self.head = 0
        self.tail = 0
        self.qsize = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.qsize != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.qsize += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.qsize -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def size(self):
        return self.qsize


if __name__ == '__main__':
    commands_num = int(input())
    max_size = int(input())
    queue_stack = MyQueueSized(max_size)
    for _ in range(commands_num):
        command = input().split()
        if command[0] == 'push':
            queue_stack.push(int(command[1]))
        if command[0] == 'pop':
            print(queue_stack.pop())
        if command[0] == 'peek':
            print(queue_stack.peek())
        if command[0] == 'size':
            print(queue_stack.size())
