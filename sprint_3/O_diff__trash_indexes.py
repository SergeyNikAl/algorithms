import random


def sorting_items(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = random.choice(numbers)
    l_nums = [num for num in numbers if num < pivot]
    pivot_nums = [pivot] * numbers.count(pivot)
    r_nums = [num for num in numbers if num > pivot]
    return sorting_items(l_nums) + pivot_nums + sorting_items(r_nums)


def count_less(numbers, desired_diff):
    count = left = 0
    for right, x in enumerate(numbers):
        while x - numbers[left] > desired_diff:
            left += 1
        count += right - left
    return count


def smallest_distance(numbers, k):
    low = 0
    high = numbers[-1] - numbers[0]
    while low < high:
        mid = (low + high) // 2
        count = count_less(numbers, mid)
        if count >= k:
            high = mid
        else:
            low = mid + 1
    return low


if __name__ == '__main__':
    input()
    print(
        smallest_distance(
            sorting_items([int(num) for num in input().split()]), int(input())
        )
    )
