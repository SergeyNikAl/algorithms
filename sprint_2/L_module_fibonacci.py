trainees, k = map(int, input().split())
fib_1 = 0
fib_2 = 1
delimeter = 10 ** k
if trainees < 2:
    fib_2 = 1
else:
    for _ in range(trainees):
        fib_1, fib_2 = fib_2, (fib_1 + fib_2) % delimeter
print(fib_2)


# def fibonacci(trainees):
#     if trainees in (0, 1):
#         return 1
#     return fibonacci(trainees - 2) + fibonacci(trainees - 1)
#
#
# if __name__ == '__main__':
#     trainees, k = map(int, input().split())
#     result = fibonacci(trainees)
#     delimeter = 10 ** k
#     print(result % delimeter if result >= delimeter else result)
