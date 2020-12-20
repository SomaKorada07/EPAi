# SESSION 3 - Numeric Types - I

## int class

- Convert a number or string to an integer, or return 0 if no arguments are given.
- If x is not a number or if base is given, then x must be a string, bytes, or bytearray instance representing an integer literal in the given base.  The literal can be preceded by '+' or '-' and be surrounded by whitespace.  ***The base defaults to 10*.**  ***Valid bases are 0 and 2-36***. Base 0 means to interpret the base from the string as an integer literal.
  - int('0b100', base=0) will result in 4.
- "int" class has many instance methods defined. We can find the details of all methods using **help(int)**. Some of them are as below:
  - \__abs__ - returns the absolute value of the number
  - \__add__ - adds two integers
  - \__eq__ - compares the values of two integers
  - \__le__ - checks for less than or equal to
  - \__lt__ - checks if one integer is less than the other



## encoded_from_base10 function

- Takes three parameters as input - number, base and digit_map and returns a string encoding in the "base" for the the "number" using the "digit_map".
- "base" should have a value between 2 and 36 both inclusive failing which a ***ValueError*** is thrown.
- Length of "digit_map" should be same as the value of base failing which a ***ValueError*** is thrown.
- "digit_map" cannot have repeated character failing which a ***ValueError*** is thrown.
- Run a while loop to find the digits corresponding to the number as per the base and then use the digit_map to get the relevant encoding.
- In case of negative numbers as input, append a '-' to the encoding obtained considering the number as positive.



## float_equality_testing function

- Takes two parameters as input - a and b and emulates the **ISCLOSE** method from the **MATH** module in a custom way (without using the MATH module).
- "***relative tolerance***" considered is 1e-12 and "***absolute tolerance***" considered is 1e-05.
- First we determine the tolerance allowed by taking the maximum of "absolute tolerance" and "relative tolerance * maximum of a,b".
- We then compute the absolute difference of a and b using the "***abs***" function.
- a and b are said to be equal if the absolute difference is less than the tolerance allowed else they are said to be not equal.



## manual_truncation_function

- Takes one parameter - f_num and emulates MATH.TRUNC method in a custom way (without using the MATH module).
- Implemented using div operator (//).



## manual_rounding_function

- Takes one parameter - f_num and emulates inbuild ROUND method in a custom way (without using the ROUND function).

- Implemented using div operator (//) and modulus operator (%).

  

## ISCLOSE method

- "isclose" is a method of "math" module.
- Parameters - *a*, *b*, *rel_tol = 1e-09*, *abs_tol = 0.0*
- Checks whether two values are close, or not. This method returns a Boolean value: `True` if the values are close, otherwise `False`.
- This method uses a relative tolerance, or an absolute tolerance, to see if the values are close.
- *rel_tol* is the relative tolerance – it is the maximum allowed difference between *a* and *b*, relative to the larger absolute value of *a* or *b*. For example, to set a tolerance of 5%, pass `rel_tol=0.05`. The default tolerance is `1e-09`, which assures that the two values are the same within about 9 decimal digits. *rel_tol* must be greater than zero.
- *abs_tol* is the minimum absolute tolerance – useful for comparisons near zero. *abs_tol* must be at least zero.
- It uses the following formula to compare the values:
  **abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)**



## MATH module

- Provides access to the mathematical functions defined by the C standard.
- These functions ***cannot be used with complex numbers***.
- Some of the functions defined in the module:
  - ***ceil*** - returns the ceiling of *x*, the smallest integer greater than or equal to *x*
  - ***fabs*** - returns the absolute value of *x*
  - ***factorial*** - returns *x* factorial as an integer
  - ***floor*** - returns the floor of *x*, the largest integer less than or equal to *x*



## ValueError

- Raised when an operation or function receives an argument that has the right type but an inappropriate value.



## round function

- Parameters - *number*, *ndigits* (optional)
- Returns *number* rounded to *ndigits* precision after the decimal point. If *ndigits* is omitted or is `None`, it returns the nearest integer to its input.
- The behavior of [`round()`](https://docs.python.org/3/library/functions.html#round) for floats can be surprising: for example, `round(2.675, 2)` gives `2.67` instead of the expected `2.68`. This is not a bug: it’s a result of the fact that most decimal fractions can’t be represented exactly as a float.



## bin() function

- Parameter - x

- Converts an integer number to a binary string prefixed with “0b”.

- ```
  format(14, '#b'), format(14, 'b')
  ('0b1110', '1110')
  >>> f'{14:#b}', f'{14:b}'
  ('0b1110', '1110')
  ```



## hex() function

- Parameter - x

- Converts an integer number to a lowercase hexadecimal string prefixed with “0x”.

- ```
  '%#x' % 255, '%x' % 255, '%X' % 255
  ('0xff', 'ff', 'FF')
  >>> format(255, '#x'), format(255, 'x'), format(255, 'X')
  ('0xff', 'ff', 'FF')
  >>> f'{255:#x}', f'{255:x}', f'{255:X}'
  ('0xff', 'ff', 'FF')
  ```
