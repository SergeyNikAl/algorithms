def comparing_two_numbers(num_1, num_2, num_type=int):
    return num_type(num_1) > num_type(num_2)


def get_max_composite_number(numbers, key=comparing_two_numbers):
    for index in range(1, len(numbers)):
        number = numbers[index]
        while index > 0 and key(number + numbers[index - 1], numbers[index - 1] + number):
            numbers[index] = numbers[index - 1]
            index -= 1
        numbers[index] = number
    return ''.join(numbers)


if __name__ == '__main__':
    input()
    print(get_max_composite_number(input().split()))