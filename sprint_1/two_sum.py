"""
Обратите внимание на ограничения в этой задаче.

Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков. Фишки лежат на столе в порядке неубывания очков на них. Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.
Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи. Помогите ей написать программу для поиска нужных фишек.

Формат ввода
В первой строке записано количество фишек n, 2 ≤ n ≤ 105.
Во второй строке записано n целых чисел в порядке неубывания —– очки на фишках Риты в диапазоне от -105 до 105.
В третьей строке —– загаданное Гошей целое число k, -105 ≤ k ≤ 105.

Формат вывода
Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.
Если таких пар несколько, то можно вывести любую из них.
Если таких пар не существует, то вывести «None».
"""

from typing import List, Tuple, Optional


def two_sum(arr: List[int], target: [int]) -> Optional[Tuple[int, int]]:
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return arr[left], arr[right]
        if total < target:
            left += 1
        else:
            right -= 1
    return None


def read_input() -> Tuple[List[int], int]:
    n = input()
    arr = list(map(int, input().strip().split()))
    target = int(input())
    return arr, target


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if not result:
        print(None)
    else:
        print(*result)


arr, target = read_input()
print_result(two_sum(arr, target))