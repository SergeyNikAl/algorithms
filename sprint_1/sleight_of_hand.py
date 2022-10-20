# ID: 70689139

from typing import Any


def get_max_points(
        keys: int, data: Any, persons=2, values='123456789'
) -> int:
    return sum(
        0 < data.count(value) <= persons * keys for value in values
    )


if __name__ == '__main__':
    print(get_max_points(
        int(input()), f'{input()}{input()}{input()}{input()}'
    ))
