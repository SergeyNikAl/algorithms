n, m = int(input()), int(input())

matrix = []

for row in range(n):
    matrix.append(map(int, input().split()))

for col in range(m):
    print(*matrix[row][col] for row in range(n))
