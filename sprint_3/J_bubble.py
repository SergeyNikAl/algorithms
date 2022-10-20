def bubble_sort(numbers):
    length = len(numbers)
    flag = True
    for index_1 in range(length - 1):
        for index_2 in range(length - index_1 - 1):
            if numbers[index_2] > numbers[index_2 + 1]:
                numbers[index_2], numbers[index_2 + 1] = numbers[index_2 + 1], numbers[index_2]
                flag = True
        if flag:
            print(*numbers)
            flag = False


if __name__ == '__main__':
    input()
    bubble_sort(list(map(int, input().split())))