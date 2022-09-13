import math

def number_of_digits(n):
    return math.floor(math.log10(n)) + 1

def is_power_of_2(n):
    return (math.log(n, 2) % 1) == 0

def halves(i):
    digits = number_of_digits(i)
    if not is_power_of_2(digits):
        # this is an assumption error
        pass

    half_1, half_2 = ((i // 10), (i % 10)) # assume it's a 2-digit number for now
    return (half_1, half_2)

