def counting_sort(nums):
    result = [abs(nums[0] - nums[-1])]
    result[1:] = [abs(nums[index] - nums[index + 1]) for index in range(1, len(nums))]
    return result


def max_sort(numbers):
    for index in range(1, len(numbers)):
        number = numbers[index]
        while index > 0 and number > numbers[index - 1]:
            numbers[index] = numbers[index - 1]
            index -= 1
        numbers[index] = number
    return numbers

def get_answer(numbers, count):
    print(numbers[count])

if __name__ == '__main__':
    input()
    get_answer(max_sort(counting_sort([int(num) for num in input().split()])),int(input()))
