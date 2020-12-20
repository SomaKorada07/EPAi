# SESSION 4 - Numeric Types - II

## Qualean class definition

**Qualean** class is inspired by Boolean+Quantum concepts. We can assign it only 3 possible **real** states - True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment we assign it a real number, it immediately finds an imaginary number **random.uniform**(-1, 1) and multiplies the input real number with the found imaginary number and stores the product internally after using Bankers rounding to 10th decimal place.



## \__init__()

- \__init__() is the constructor of the Qualean class.
- Takes only one argument which is the real state - can be either 0 or 1 or -1.
- Internally generates the imaginary number by randomly picking a number between -1 and 1.
- Multiplies the real state with the imaginary number and stores the product rounding off to 10 digits using the Banker's rounding mechanism.



## \__repr__()

- \__repr__() is the representation function of the Qualean class.
- It returns the stored number as a string.
- It is called when we try to print the object using "print()".



## \__str__()

- \__str__() is the string function of Qualean class.
- It also returns the stored number as a string.



## \__eq__()

- \__eq__() is used to check if two Qualean numbers are same.
- Takes another Qualean object or number type or string as an argument.
- Uses '==' operator to check if two Qualean numbers are same.



## \__ge__()

- \__ge__() is used to check if the Qualean number is greater than or equal to another Qualean number.
- Takes another Qualean object or number type or string as an argument.
- Uses '>=' operator to check the condition.



## \__gt__()

- \__gt__() is used to check if the Qualean number is greater than another Qualean number.
- Takes another Qualean object or number type or string as an argument.
- Uses '>' operator to check the condition.



## \__le__()

- \__le__() is used to check if the Qualean number is less than or equal to another Qualean number.
- Takes another Qualean object or number type or string as an argument.
- Uses '<=' operator to check the condition.



## \__lt__()

- \__lt__() is used to check if the Qualean number is less than or equal to another Qualean number.
- Takes another Qualean object or number type or string as an argument.
- Uses '<' operator to check the condition.



## \__add__()

- \__add__() is used to add two Qualean numbers.
- Takes another Qualean object or number type or string as an argument.
- Uses '+' operator to perform the operation.



## \__mul__()

- \__mul__() is used to multiply two Qualean numbers.
- Takes another Qualean object or number type or string as an argument.
- Uses '*' operator to perform the operation.



## \__sqrt__()

- \__sqrt__() is used to find the square root of the Qualean number.
- Takes no argument.
- In case of negative Qualean number, returns a complex number as the square root.



## \__bool__()

- \__bool__() returns false if the Qualean number is 0 else returns True.



## \__float__()

- \__float__() returns the floating value of the Qualean number.



## \__invertsign__()

- \__invertsign__() return the Qualean object with the number having the negated sign.



## \__and__()

- \__and__() implements the Short Circuiting principle in Python.

  def __and__(self, other):
      if not bool(self.number):
          return self.number
      if not isinstance(other, Qualean):
          raise TypeError("Expected type Qualean.")
      return (self.number) and (other.number)



## \__or__()

- \__or__() implements the Short Circuiting principle in Python.

  def __or__(self, other):
      if bool(self.number):
          return self.number
      if not isinstance(other, Qualean):
          raise TypeError("Expected type Qualean.")
      return (self.number) or (other.number)



## Test Results

![](C:\EPAi\sesssion4-SomaKorada07\TestResults.JPG)
