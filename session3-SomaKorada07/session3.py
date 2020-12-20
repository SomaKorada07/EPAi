from fractions import Fraction

def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    repeating_check = False
    for i in digit_map:
        if digit_map.count(i) > 1:
            repeating_check = True
    if 2 <= base and base <= 36 and len(digit_map) == base and not repeating_check:
        pass
    else:
        raise ValueError('the base should be between 2 and 36 both inclusive or there is a repeating character in digit_map')

    if number == 0:
        return '0'

    new_number = abs(number)

    digits = []

    while new_number > 0:
        m = new_number % base
        new_number = new_number // base
        digits.insert(0,m)

    result = ''

    for digit in digits:
        if digit <= len(digit_map):
            result = result + str(digit_map[digit])
        else:
            result = result + str(digit_map[len(digit_map) % digit])

    if number < 0:
        result = '-' + result

    return result


def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05

    tol = max((rel_tol * max(a,b)), abs_tol)

    if abs(a - b) < tol:
        return True
    else:
        return False


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    if type(f_num) != 'str':
        if f_num >= 0:
            x = f_num // 1
        else:
            x = (f_num // 1) + 1
 
    return x

def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    if type(f_num) != 'str':
        if f_num > 0:
            trunc = f_num // 1
            decimal = f_num % trunc
            if decimal >= 0.5:
                x = trunc + 1
            else:
                x = trunc
        elif f_num == 0:
            x = 0
        else:
            trunc = (f_num // 1) + 1
            decimal = f_num % trunc
            if decimal >= -0.5:
                x = trunc
            else:
                x = trunc + 1

    return x

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    return 3.0