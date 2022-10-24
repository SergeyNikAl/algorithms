# ID: 71220160

DEQUE_IS_EMPTY = 'Дек пуст. Отсутствуют элементы для удаления.'
DEQUE_IS_FULL = 'Дек переполнен.'
COMMAND_ERROR = 'Команда {command} не предусмотрена.'


class Deque:

    def __init__(self, max_size):
        self._items = [None] * max_size
        self._max_size = max_size
        self._head = 0
        self._tail = -1
        self._size = 0

    def __is_empty(self):
        return self._size == 0

    def __is_full(self):
        return self._size == self._max_size

    def push_front(self, value):
        if self.__is_full():
            raise IndexError(DEQUE_IS_FULL)
        self._head = (self._head - 1) % self._max_size
        self._items[self._head] = value
        self._size += 1

    def push_back(self, value):
        if self.__is_full():
            raise IndexError(DEQUE_IS_FULL)
        self._tail = (self._tail + 1) % self._max_size
        self._items[self._tail] = value
        self._size += 1

    def pop_front(self):
        if self.__is_empty():
            raise IndexError(DEQUE_IS_EMPTY)
        value = self._items[self._head]
        self._head = (self._head + 1) % self._max_size
        self._size -= 1
        return value

    def pop_back(self):
        if self.__is_empty():
            raise IndexError(DEQUE_IS_EMPTY)
        value = self._items[self._tail]
        self._tail = (self._tail - 1) % self._max_size
        self._size -= 1
        return value


def main(deque, commands):
    data = []
    for command in commands:
        try:
            method, *params = command
            result = getattr(deque, method)(*params)
            if result:
                data.append(result)
        except IndexError:
            data.append('error')
        except AttributeError:
            raise ValueError(COMMAND_ERROR.format(command=command))
    return data


if __name__ == '__main__':
    commands_count = int(input())

    print(
        *main(
            deque=Deque(int(input())),
            commands=[input().split() for _ in range(commands_count)]
        ),
        sep='\n'
    )
