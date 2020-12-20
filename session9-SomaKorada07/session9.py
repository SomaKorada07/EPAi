import datetime
import time
from functools import wraps
from functools import reduce
from functools import singledispatch
from html import escape
from numbers import Integral
from decimal import Decimal

def odd_run(fn : "Function"):
	"""
	Decorator to allow a function to run only on odd seconds.
	"""
	@wraps(fn)
	def run_func(*args, **kwargs):
		if (datetime.datetime.now().time().second % 2 != 0):
			return fn(*args, **kwargs)
		else:
			print('Sorry, time is in even secs. Cannot run the function!')

	return run_func



def log_decorator(fn : "Function"):
	"""
	Decorator to log the function calls.
	"""
	from datetime import datetime, timezone

	@wraps(fn)
	def add_log(*args, **kwargs):
		start_time = datetime.now(timezone.utc)
		result = fn(*args, **kwargs)
		end_time = datetime.now(timezone.utc)
		print(f'{start_time}: called {fn.__name__} with execution time {start_time - end_time}')
		return result
	
	return add_log



def authenticate(current_password: str, user_password: str):
    """
    Wrapper used to authenticate the function before executing the function.
    curr_password: `set_password` closure to get password from user.
    :param user_password: pre-defined password compared with the `curr_password`.
    """ 
    current_password = "TSAI@Welcome"
    def authenticate_decorator(fn):
    	"""

    	"""
    	@wraps(fn)
    	def inner(*args, **kwargs):
    		if(user_password == current_password):
    			return fn(*args, **kwargs)
    		else:
    			print('Sorry, you are not authorized!')
    	return inner

    return authenticate_decorator



def timed(times : int):
	"""
	Decorator to count number of times a function is called
	"""
	from time import perf_counter
	from functools import wraps

	def timed_decorator(fn):
		@wraps(fn)
		def count_function_calls(*args, **kwargs):
			elapsed_total = 0
			elapsed_count = 0

			for i in range(times):
				start = perf_counter()
				result = fn(*args, **kwargs)
				end = perf_counter()
				elapsed = end - start
				elapsed_total += elapsed
				elapsed_count += 1

			elapsed_avg = elapsed_total / elapsed_count

			print(f'{fn.__name__} took {elapsed_avg} seconds')

			return result

		return count_function_calls

	return timed_decorator



class privilegeDecorator:
	"""
	Decorator to provide privilege access 
	(has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params)
	"""
	def __init__(self, privilege = 'no'):
		self.privilege = privilege

	def __call__(self, fn):
		@wraps(fn)
		def set_privilege(**kwargs):
			arguments = list(kwargs.items())
			if self.privilege == "high":
				return fn(**dict(arguments[:4]))
			elif self.privilege == "mid":
				return fn(**dict(arguments[:3]))
			elif self.privilege == "low":
				return fn(**dict(arguments[:2]))
			elif self.privilege == "no":
				return fn(**dict(arguments[:1]))

		return set_privilege



@singledispatch
def htmlize(input_str: str) -> str:
    """
    Converts the newline character in a string to contain a br tag.
    input: string to escape.
    return: string, transformed
    """
    return escape(str(input_str)).replace("\n", "<br/>\n")



@htmlize.register(Integral)
def html_integral_numbers(input_int: int) -> str:
    """
    Convert the integral numbers to proper format.
    input: Integer to convert
    return: htmlized integer
    """
    return f"{input_int}(<i>{str(hex(input_int))}</i>)"



@htmlize.register(Decimal)
@htmlize.register(float)
def html_real(input_float: float) -> str:
    """
    Converts the real number to rounded real number with precision of 2.
    int: float number to convert
    return: htmlized float
    """
    return f"(<i>{round(input_float, 2)}</i>)"



@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(input_seq: "Sequence") -> str:
    """
    Converts the python sequence (tuples and lists) to an unordered list
    input: sequence
    output: unordered list
    """
    items = (f"<li>{htmlize(item)}</li>" for item in input_seq)
    return "<ul>\n" + "\n".join(items) + "\n</ul>"



@htmlize.register(dict)
def html_dict(input_dict: dict) -> str:
    """
    Converts python dictionary to an un ordered list
    input: dictionary object to convert
    output: unordered list
    """
    items = (f"<li>{k}={v}</li>" for k, v in input_dict.items())
    return "<ul>\n" + "\n".join(items) + "\n</ul>"