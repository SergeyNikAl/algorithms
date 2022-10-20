def merge(numbers, left, mid, right):
    if len(numbers) == 1:
        return numbers
    numbers_1 = numbers[left:mid]
    numbers_2 = numbers[mid:right]
    result = []
    l, r = 0, 0
    while l < len(numbers_1) and r < len(numbers_2):
        if numbers_1[l] <= numbers_2[r]:
            result.append(numbers_1[l])
            l += 1
        else:
            result.append(numbers_2[r])
            r += 1
    if l < len(numbers_1):
        result += numbers_1[l:]
    else:
        result += numbers_2[r:]
    return result


def merge_sort(numbers, left, right):
    if right - left >= 2:
        mid = (left + right) // 2
        merge_sort(numbers, left, mid)
        merge_sort(numbers, mid, right)
        numbers[left:right] = merge(numbers, left, mid, right)



def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
