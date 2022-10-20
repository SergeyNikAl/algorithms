from typing import List


def factorize(number: int, divisor=2) -> List[int]:
    result = []
    while divisor ** 2 <= number:
        if number % divisor == 0:
            number //= divisor
            result.append(divisor)
        else:
            divisor += 1
    if number != 1:
        result.append(number)
    return result


print(*factorize(int(input())))