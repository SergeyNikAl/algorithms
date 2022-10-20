#def calculate_value_at_point(a: int, x: int, b: int, c: int, degree=2) -> int:
#    return a * x ** degree + b * x + c
#

#print(calculate_value_at_point(*list(map(int, input().strip().split()))))

print(
    (lambda a, x, b, c: a * x ** 2 + b * x + c)
    (*list(map(int, input().strip().split())))
)
