def get_segments(segments):
    segments.sort()
    for index in range(len(segments) - 1):
        if segments[index + 1][0] <= segments[index][1]:
            determinant = segments[index][1] < segments[index + 1][1]
            segments[index + 1][0] = segments[index][0]
            segments[index + 1][1] = segments[index + determinant][1]
            segments[index] = []
    return segments


def print_answer(segments):
    for segment in segments:
        if segment:
            print(*segment)


if __name__ == '__main__':
    print_answer(get_segments(
        [list(map(int, input().split())) for _ in range(int(input()))]
    ))