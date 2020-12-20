# SESSION 2 - Object Mutability and Interning

## Something class

- "Something" class has one instance variable and two instance methods.
- Instance variable defined is as below:
  - something_new
- Instance methods defined are as below:
  - \__init__ - Used to initialize the instance variables. Does not have any parameters.
  - \__repr__ - Stands for "representation". Used for returning a printable version of the object

## SomethingNew class

- "SomethingNew" class has two instance variables and two instance methods.
- Instance variable defined is as below:
  - i - "int" is the type defined as convention but it is not a must that the argument should be referencing an "int"
  - something - "Something" class is the type defined as convention but it is not a must that the argument should be referencing to "Something" class
- Instance methods defined are as below:
  - \__init__ - Has two parameters - 'i' and 'something'.
  - \__repr__

## add_something function

- "add_something" function takes two parameters - 'collection' and 'i'.
- "collection" - "List[Something]" is the type defined as convention but it is not a must that the argument should be referencing to a list.
- Creates an instance of "Something" class.
- Assigns an instance of "SomethingNew" class to "something_new" instance variable of "Something" class creating a circular reference.
- Populates the "collection" list with instance of "Something" class.

## clear_memory function

- "clear_memory" function takes one parameter - 'collection'.
- Clears the 'collection' list.
- Explicitly calls Garbage Collector to remove circular reference created.

## critical_function function

- Assigns 'collection' to a list.
- Runs an iterative loop to call 'add_something" function for 1024 * 128 times.
- Finally calls "clear_memory" function.

## compare_strings_old function

- "compare_strings_old" function takes a number 'n' as parameter. 
- Defines two strings 'a' and 'b' whose value is same.
- Runs a loop for 'n' iterations to check if the strings 'a' and 'b' have same value by using "==" operator. "==" operator checks for the values which in this case are strings and hence the comparison operation takes a long time for computation.
- Converts the string 'a' into a list of characters and stores in a variable "**char_list**".
- Runs a loop for 'n' iterations to check if the character 'd' is present in the list of characters from string 'a' ("char_list").

## compare_strings_new function

- "compare_strings_new" function takes a number 'n' as parameter.
- Defines two strings 'a' and 'b' whose value is same.
- Checks if the strings 'a' and 'b' are same by using "is" operator. "is" operator checks for the address which is an int and hence the comparison operation takes very minimal time for computation.
- Runs a loop for number of characters in 'a' to check if the character 'd' matches with each character in the iteration.

## sleep function

- "sleep" is a standard function defined in the "time" module.
- Takes a number as a parameter which denotes the number of seconds.
- Used to halt the execution of the program.
- On Windows, the smallest interval for "sleep" function allowed is 10 - 13 milliseconds.

