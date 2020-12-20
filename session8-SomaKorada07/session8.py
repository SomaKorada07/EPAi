def check_docstring(fn) -> "function":
	"""
	This closure takes a function as input and checks if the input function has a docstring more than 50 characters.

	# Input : function fn

	# Output : function inner

	# Functionality : Defines a free variable with value 50. Defines another function which tests if input function has 
					  a docstring with more than 50 characters.
	"""
	length = 50
	def cal_docstring() -> bool:
		"""
		Checks for the input function's docstring length and returns True if it is more than 50 else False.
		"""
		return bool(len(fn.__doc__) > length)
	return cal_docstring



def next_fibonacci():
	"""
	This closure gives the next Fibonacci number.

	# Input : no input

	# Output : function inner

	# Functionality : Defines 2 free variables - x and y. Defines another function which calculates the next fibonacci
					  number.
	"""
	x = 0
	y = 1
	def cal_fibonacci():
		"""
		Determines next fibonacci number and recalculates x and y accordingly. Returns the next Fibonacci number.
		"""
		nonlocal x, y
		fib = x + y
		x = y
		y = fib
		return fib
	return cal_fibonacci


def add(a, b):
	"""
	returns addition of 2 input numbers
	"""
	return a + b


def mul(a, b):
	"""
	returns multiplication of 2 input numbers
	"""
	return a * b


def sub(a, b):
	"""
	returns subtraction of 2 input numbers
	"""
	return a - b


def div(a, b):
	"""
	returns division of 2 input numbers
	"""
	if not bool(b):
		return a / b


func_counter = {}
def fn_counter(fn) -> "function":
	"""
	This closure keeps a track of how many times a function was called and updates a global dictionary with the counts.

	# Input : function fn

	# Output : function inner

	# Functionality : Defines a global dictionary - func_counter and a free variable - cnt. Defines another function which
					  increments the free variable whenever the function fn is called and stores in func_counter.
	"""
	cnt = 0
	def increment_counter(*args, **kwargs):
		"""
		Increments the free variable for the function fn and updates the global dictionary.
		"""
		nonlocal cnt
		global func_counter
		cnt += 1
		func_counter[fn.__name__] = cnt
		return fn(*args, **kwargs)
	return increment_counter



def fn_user_counter(fn, user_dict) -> "function":
	"""
	This closure is updated version of the above. It takes in a specific dictionary to update the counts.

	# Input : function fn and dictionary user_dict

	# Output : function inner

	# Functionality : Takes a function fn and dictionary user_dict as inputs. Defines another function to update the input
					  dictionary with the count for the specific function fn.
	"""
	def increment_user_counter(*args, **kwargs):
		"""
		Updates the input dictionary with the count for the specific function fn.
		"""
		user_dict[fn.__name__] += 1
		return fn(*args, **kwargs)
	return increment_user_counter
