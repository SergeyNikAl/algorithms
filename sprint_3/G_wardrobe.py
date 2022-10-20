def counting_sort(things, key=3):
    counted_values = [0] * key
    for thing in things:
        counted_values[thing] += 1
    things[0:] = [val for val in range(key) for _ in range(counted_values[val])]
    return things


if __name__ == '__main__':
    input()
    print(*counting_sort(list(map(int, input().split()))))