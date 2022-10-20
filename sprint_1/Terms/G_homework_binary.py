from typing import Any


def to_binary(number: int) -> Any[str, int]:
    result = ''
    if number == 0:
        return 0
    while number > 0:
        result = str(number % 2) + result
        number //= 2
    return result


if __name__ == '__main__':
    print(to_binary(int(input().strip())))
