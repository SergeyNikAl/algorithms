def two_bicycle(piggy_bank, cost, left=0, right=0):
    if left >= right:
        return -1
    mid = (left + right) // 2
    if piggy_bank[mid] >= cost > piggy_bank[mid - 1] or mid == 0:
        return mid + 1
    if cost <= piggy_bank[mid]:
        return two_bicycle(piggy_bank, cost, left, right=mid)
    else:
        return two_bicycle(
            piggy_bank, cost, left=mid + 1, right=len(piggy_bank)
        )


if __name__ == '__main__':
    input()
    piggy_bank = list(map(int, input().split()))
    cost = int(input())
    day_1 = two_bicycle(piggy_bank, cost, left=0, right=len(piggy_bank))
    day_2 = two_bicycle(piggy_bank, cost * 2, left=0, right=len(piggy_bank))
    print(day_1, day_2)
