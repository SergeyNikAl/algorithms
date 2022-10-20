# ID:70694072

from typing import Any, List


def get_distances(house_numbers: Any, separator='0') -> List[int]:
    """
    Рассчет минимального расстояния между домами и пустыми участками
    :param house_numbers: Массив с номерами домов с учетом пустых участков;
    :param separator: Значение для нахождения индекса пустого участка в массиве;
    :return: Массив с минимальным расстоянием от каждого дома до пустого участка;
    """
    result = [0] * len(house_numbers)
    zeroes = [
        index for index, value in enumerate(house_numbers)
        if value == separator
    ]
    first, last = zeroes[0], zeroes[-1]
    result[:first] = [first - index for index in range(first)]
    for left, right in zip(zeroes, zeroes[1:]):
        result[left + 1: right] = [
            min(pos - left, right - pos) for pos in range(left + 1, right)
        ]
    result[last + 1:] = [
        index - last for index in range(last + 1, len(house_numbers))
    ]

    return result


if __name__ == '__main__':
    input()
    print(*get_distances(input().split()))
