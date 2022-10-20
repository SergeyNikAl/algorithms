def is_power_of_four(number: int, divider=4) -> bool:
    while number > 1:
        if number % divider != 0:
            return False
        number //= divider
    return True


print(is_power_of_four(int(input())))
