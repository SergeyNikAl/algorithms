from typing import Any


def check_parity(nums) -> Any:
    data = []
    for num in nums:
        if num % 2 == 1:
            data.append(num)
    return 'WIN' if not data or len(data) == len(nums) else 'FAIL'


if __name__ == '__main__':
    print(check_parity(list(map(int, input().strip().split()))))
