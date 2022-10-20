from typing import List


def get_weather_randomness(data: List[int]) -> int:
    counter = 0
    if len(data) == 1:
        return counter + 1
    if data[0] > data[1]:
        counter += 1
    if data[-2] < data[-1]:
        counter += 1
    for i in range(1, len(data) - 1):
        if data[i - 1] < data[i] > data[i + 1]:
            counter += 1
    return counter


input()
print(get_weather_randomness(list(map(int, input().strip().split()))))
