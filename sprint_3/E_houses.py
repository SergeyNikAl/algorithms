import random


def sorting_items(houses_price):
    if len(houses_price) <= 1:
        return houses_price
    pivot = random.choice(houses_price)
    l_price = [price for price in houses_price if price < pivot]
    pivot_price = [pivot] * houses_price.count(pivot)
    r_price = [price for price in houses_price if price > pivot]
    return sorting_items(l_price) + pivot_price + sorting_items(r_price)


def houses(budget, houses_price):
    count = 0
    total = budget[1]
    for price in houses_price:
        if price > total:
            return count
        total -= price
        count += 1
    return count


if __name__ == '__main__':
    print(houses(
        list(map(int, input().split())), sorting_items(list(map(int, input().split())))
    ))