"""
Обратите внимание на ограничения в этой задаче.

Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков.
Фишки лежат на столе в порядке неубывания очков на них. Сначала Гоша называет число k,
затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.
Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи.
Помогите ей написать программу для поиска нужных фишек.

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


def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    nums_set = set(nums)
    for indx, val in enumerate(nums):
        diff = target - val
        try:
            if diff in nums_set and indx != nums.index(diff, indx + 1):
                return val, diff
        except:
            continue


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if not result:
        print(None)
    else:
        print(*result)


if __name__ == '__main__':
    input()
    print_result(
        two_sum(list(map(int, input().strip().split())), int(input()))
    )