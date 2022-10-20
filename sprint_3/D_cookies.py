import random


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    q = random.choice(nums)
    l_nums = [n for n in nums if n > q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n < q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


def happy_children(children, cookies):
    happy_children = 0
    idx_cookie = 0
    for index in range(len(children)):
        if idx_cookie < len(cookies) and children[index] <= cookies[idx_cookie]:
            happy_children += 1
            idx_cookie += 1
    return happy_children


if __name__ == '__main__':
    input()
    children = quicksort([int(num) for num in input().split()])
    input()
    cookies = quicksort([int(num) for num in input().split()])
    print(happy_children(children, cookies))