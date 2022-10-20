def fibonacci(trainees):
    if trainees in (1, 2):
        return 1
    return fibonacci(trainees - 1) + fibonacci(trainees - 2)

if __name__ == '__main__':
    print(fibonacci(int(input())))