import math

# NOTE: conditions are checks in algorithm implementation NOT in helper functions themselves
# (aside from obvious error check) for clarity and ease of implementation

# helper functions
def number_of_digits(n):
    if n == 0:
        return 1
    else:
        return math.floor(math.log10(n)) + 1

def is_power_of_2(n):
    return (math.log(n, 2) % 1) == 0

def halves(i):
    digits = number_of_digits(i)

    half_1, half_2 = ( (i // (10**(digits//2))), (i % 10**(digits//2)) )
    return (half_1, half_2)

def error_check_and_get_number_of_digits(x, y):
    if x < 0 or y < 0:
        raise InputError(f"x, y must be positive, NOT (x={x}, y={y})!")
    
    x_digits, y_digits = number_of_digits(x), number_of_digits(y)
    # error checks
    if not x_digits == y_digits:
        raise InputError(f"x,y must have the same number of digits, NOT ({x_digits}, {y_digits})!")
    
    if not is_power_of_2(x_digits):
        raise AssumptionError(f"x must be a n-digit integer, where n is power of 2, NOT (n={x_digits})")
    
    return x_digits

# exceptions
class InputError(Exception):
    """ Input: two n-digit positive integers"""
    
class AssumptionError(Exception):
    """Assumption: n is power of 2 """
    
# algorithms
def recursive_integer_multiplication(x, y):
    """
    Input:      two n-digit positive integers
    Output:     the product x*y
    Assumption: n is power of 2
    """
    # error checks
    n = error_check_and_get_number_of_digits(x, y)
    
    # implementation
    if n == 1:
        return x * y
    else:
        a, b = halves(x)
        c, d = halves(y)
        
        ac, ad, bc, bd = (
            recursive_integer_multiplication(a,c), 
            recursive_integer_multiplication(a,d), 
            recursive_integer_multiplication(b,c), 
            recursive_integer_multiplication(b,d)
        )
        return (10**n * ac) + (10**(n//2) * (ad + bc) + bd)
    
    
def karatsuba(x, y):
    """
    Input:      two n-digit positive integers
    Output:     the product x*y
    Assumption: n is power of 2
    """
    # error checks
    n = error_check_and_get_number_of_digits(x, y)
    
    # implementation
    if n == 1:
        return x * y
    else:
        a, b = halves(x)
        c, d = halves(y)

        p, q = (a+b), (c+d)
        ac, bd = (
            karatsuba(a, c),
            karatsuba(b, d)
        )
        adbc = (p*q) - ac - bd
    
    return (10**n * ac) + (10**(n//2) * adbc + bd)
    