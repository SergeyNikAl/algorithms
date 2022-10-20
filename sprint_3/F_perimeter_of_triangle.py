import random


def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    q = random.choice(numbers)
    l_nums = [n for n in numbers if n > q]
    e_nums = [q] * numbers.count(q)
    r_nums = [n for n in numbers if n < q]
    return quicksort(l_nums) + e_nums + quicksort(r_nums)


def get_perimeter(numbers):
    for index in range(len(numbers)):
        if numbers[index] < (numbers[index + 1] + numbers[index + 2]):
            return numbers[index] + numbers[index + 1] + numbers[index + 2]


if __name__ == '__main__':
    input()
    print(get_perimeter(quicksort(list(map(int, input().split())))))