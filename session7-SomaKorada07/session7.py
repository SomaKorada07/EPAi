import math
import random
from functools import reduce, partial


# A pre-calculated list to store fibonacci numbers till 10000
fibonacci_numbers = [0, 1]
while fibonacci_numbers[-1] + fibonacci_numbers[-2] < 10000:
    fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])


# A function using only list filter lambda that can tell whether a number is a Fibonacci number or not
check_fibonacci = lambda l : list(filter(lambda x: x in fibonacci_numbers, l))


# List comprehension to add 2 iterables a and b such that a is even and b is odd
add_even_odd = lambda a, b : [x + y for x, y in zip(a, b) if x % 2 == 0 and y % 2 != 0]


# List comprehension to strip every vowel from a string provided
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', '0', 'U']
strip_vowels = lambda s : [x for x in s if x not in vowels]


# List comprehension to act like a ReLU function for a 1D array
relu_func = lambda l : [x if x > 0 else 0 for x in l]


# List comprehension to act like a sigmoid function for a 1D array
sigmoid_func = lambda l : [(1 / (1 + math.exp(-x))) for x in l]


# List comprehension that takes a small character string and shifts all characters by 5
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shift_characters = lambda s : "".join([alphabets[alphabets.index(x) + 5] if alphabets.index(x) < 21 else alphabets[alphabets.index(x) - 26 + 5] for x in s])


# List comprehension to check if given input has any swear words
with open("swear_words.txt", "r") as f:
    swear_words = f.read().split()

check_swear_words = lambda s : any([word for word in s.split() if word.lower() in swear_words])


# Reduce function to add only even numbers in a list
add_even_numbers = lambda l : reduce(lambda a, b: a + b if b % 2 == 0 else a, l, 0)


# Reduce function to find the biggest character in a string
find_biggest_character = lambda s : reduce(lambda x, y: x if ord(x) > ord(y) else y, s)


# Reduce function to add every 3rd number in a list
add_third_element = lambda l : reduce(lambda x, y: x + y, l[2::3], 0)


# An expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999
generate_number_plate = lambda : [f"KA{random.randint(10, 99)}{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}{random.randint(1000, 9999)}" for i in range(15)]


# Partial function to let user input state ID and plate number
random_plates = lambda st='KA', number_plate='1234' : [f"{st}{random.randint(10, 99)}{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}{number_plate}" for i in range(15)]

random_plates_partial = partial(random_plates, st = 'DL', number_plate = '7777')
