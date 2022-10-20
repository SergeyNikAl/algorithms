# def merge_sort(data_1, data_2):
#     population = []
#     first, second = 0, 0
#     while first < len(data_1) and second < len(data_2):
#         if data_1[first] < data_2[second]:
#             population.append(data_1[first])
#             first += 1
#         else:
#             population.append(data_2[second])
#             second += 1
#     if first < len(data_1):
#         population += data_1[first:]
#     else:
#         population += data_2[second:]
#     return population
#
#
# def get_median(population):
#     size = len(population)
#     mid = size // 2
#     return (population[mid - 1] + population[mid]) / 2 if size % 2 == 0 else population[size // 2]
#
#
# if __name__ == '__main__':
#     input()
#     input()
#     print(get_median(merge_sort(
#         [int(num) for num in input().split()],
#         [int(num) for num in input().split()]
#     )))



def gen_merge_inner(pop_1, pop_2):
    population_1 = next(pop_1, None)
    population_2 = next(pop_2, None)
    while population_1 is not None or population_2 is not None:
        if population_1 is None or (
                population_2 is not None and population_2 < population_1):
            yield population_2
            population_2 = next(pop_2, None)
        else:
            yield population_1
            population_1 = next(pop_1, None)


def gen_merge(list1, list2):
    return list(gen_merge_inner(iter(list1), iter(list2)))


def get_median(population):
    size = len(population)
    mid = size // 2
    return (population[mid - 1] + population[mid]) / 2 if size % 2 == 0 else \
    population[size // 2]


if __name__ == '__main__':
    input()
    input()
    print(get_median(gen_merge(
        list(map(int, input().split())), list(map(int, input().split()))
    )))


#_____________________________________________________________________________

# def merge_sort(data_1, data_2):
#     population = []
#     first, second = 0, 0
#     while first < len(data_1) and second < len(data_2):
#         if data_1[first] < data_2[second]:
#             population.append(data_1[first])
#             first += 1
#         else:
#             population.append(data_2[second])
#             second += 1
#     result_start = first + second
#     if first < len(data_1):
#         population[result_start + 1:] = [data_1[index] for index in range(first, len(data_1))]
#     else:
#         population[result_start + 1:] = [data_2[index] for index in range(second, len(data_2))]
#     return population
#
#
# def get_median(population):
#     size = len(population)
#     mid = size // 2
#     return (population[mid - 1] + population[mid]) / 2 if size % 2 == 0 else population[size // 2]
#
#
# if __name__ == '__main__':
#     input()
#     input()
#     print(get_median(merge_sort(
#         list(map(int, input().split())), list(map(int, input().split()))
#     )))

#_____________________________________________________________________________

# def quicksort(population):
#     if len(population) <= 1:
#         return population
#     else:
#         q = random.choice(population)
#     l_nums = [n for n in population if n < q]
#
#     e_nums = [q] * population.count(q)
#     b_nums = [n for n in population if n > q]
#     return quicksort(l_nums) + e_nums + quicksort(b_nums)
#
#
# def get_median(population):
#     size = len(population)
#     mid = size // 2
#     return (population[mid - 1] + population[mid]) / 2 if size % 2 == 0 else population[size // 2]
#
#
# if __name__ == '__main__':
#     input()
#     input()
#     population = list(map(int, input().split())) + list(map(int, input().split()))
#     print(get_median(quicksort(population)))