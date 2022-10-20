from typing import List


def get_sum(numbers: List[str], k: int) -> int:
    return int(''.join(numbers)) + k


if __name__ == '__main__':
    input()
    print(*list(str(get_sum(input().strip().split(), int(input())))))
