# ID: 72631393

def quick_sort(candidates):
    length = len(candidates)

    def sorting(start, end):
        if start >= end:
            return
        pivot = candidates[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while candidates[left] < pivot:
                left += 1
            while pivot < candidates[right]:
                right -= 1
            if left <= right:
                (
                    candidates[left], candidates[right]
                ) = (
                    candidates[right], candidates[left]
                )
                left += 1
                right -= 1
        sorting(start, right)
        sorting(left, end)

    sorting(0, length - 1)
    return candidates


if __name__ == '__main__':
    print(
        *[name for _, _, name in quick_sort([
            (lambda name, tasks, penalty:
                (-int(tasks), int(penalty), name)
            )(
                *input().split()
            ) for _ in range(int(input()))
        ])],
        sep='\n',
    )


# class Candidate:
#
#     def __init__(self, name, tasks, penalty, value_type=int):
#         self.name = name
#         self.tasks = value_type(tasks)
#         self.penalty = value_type(penalty)
#
#     def __str__(self):
#         return self.name
#
#     def __lt__(self, other):
#         if isinstance(other, Candidate):
#             return (
#                 -self.tasks, self.penalty, self.name
#             ) < (
#                 -other.tasks, other.penalty, other.name
#             )
#
# def quick_sort(candidates):
#     length = len(candidates)
#
#     def sorting(start, end):
#         if start >= end:
#             return
#         pivot = candidates[(start + end) // 2]
#         left, right = start, end
#         while left <= right:
#             while candidates[left] < pivot:
#                 left += 1
#             while pivot < candidates[right]:
#                 right -= 1
#             if left <= right:
#                 (
#                     candidates[left], candidates[right]
#                 ) = (
#                     candidates[right], candidates[left]
#                 )
#                 left += 1
#                 right -= 1
#         sorting(start, right)
#         sorting(left, end)
#
#     sorting(0, length - 1)
#     return candidates
#
#
# if __name__ == '__main__':
#     print(*quick_sort([
#         Candidate(*input().split()) for _ in range(int(input()))
#     ]), sep='\n')