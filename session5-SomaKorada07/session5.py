import time
import math
from decimal import Decimal


def time_it(fn, *args, repetitions = 1, **kwargs):

    if repetitions <= 0:
        raise ValueError('Repetitions should be a positive integer > 0.')

    if type(repetitions) != int:
        raise TypeError('Repetitions should be an integer!')

    start_time = time.time()

    for i in range(repetitions):
        fn(*args, **kwargs)

    end_time = time.time()

    print(f'Average run time per call is {(end_time - start_time) / repetitions}')


def squared_power_list(*args, **kwargs):

    for i in args:
        number = i

    start = kwargs['start']

    end = kwargs['end']

    if type(number) != int:
        raise TypeError('Number should be an integer!')

    if number <= 0:
        raise ValueError('Number has to be positive integer > 0.')

    if type(start) != int:
        raise TypeError('Start should be an integer!')

    if (start < 0 or start > 5):
        raise ValueError('Start has to be positive integer between 0 and 5 both inclusive.')

    if type(end) != int:
        raise TypeError('End should be an integer!')

    if (end < 0 or end > 15):
        raise ValueError('End has to be positive integer between 0 and 15 both inclusive.')

    result = []

    for i in range(start, end + 1):
        result.append(number ** i)

    return result
    #print(f'squared_power_list is {result}')



def polygon_area(*args, **kwargs):

    for i in args:
        side_length = i

    num_sides = kwargs['sides']

    if type(side_length) not in [int, float, Decimal]:
        raise TypeError('Length of the side should be an integer or float or Decimal!')

    if side_length <= 0:
        raise ValueError('Length of side has to be positive number > 0.')

    if type(num_sides) != int:
        raise TypeError('Number of sides should be an integer!')

    if (num_sides < 3 or num_sides > 6):
        raise ValueError('Number of sides has to be positive integer between 3 and 6 both inclusive.')

    area = ((side_length ** 2) * num_sides) / (4 * math.tan(math.pi / num_sides))

    return area
    #print(f'area is {area}')



def temp_converter(*args, **kwargs):

    for i in args:
        given_temp = i
 
    given_unit = kwargs['temp_given_in']

    if type(given_temp) not in [int, float, Decimal]:
        raise TypeError('Given temperature is not a number!')

    if given_unit not in ['f', 'c']:
        raise ValueError('Given unit is neither in Celsius nor in Fahrenheit.')

    if given_unit == 'f':
        converted_temp = (given_temp - 32) * 5 / 9
    else:
        converted_temp = (given_temp * 9 / 5) + 32

    return converted_temp
    #print(f'converted_temp is {converted_temp}')



def speed_converter(*args, **kwargs):

    for i in args:
        given_speed = i

    given_distance = given_speed
    given_time = 1

    distance_unit = kwargs['dist']
    time_unit = kwargs['time']

    if type(given_speed) not in [int, float, Decimal]:
        raise TypeError('Given temperature is not a number!')

    if distance_unit not in ['km', 'm', 'ft', 'yrd']:
        raise ValueError('Distance unit is neither kilometer, meter, feet nor yard!')

    if time_unit not in ['ms', 's', 'min', 'hr', 'day']:
        raise ValueError('Time unit is neither millisecond, second, minute, hour nor day!')

    if distance_unit == 'km':
        converted_dist = given_distance
    elif distance_unit == 'm':
        converted_dist = given_distance * 1000
    elif distance_unit == 'ft':
        converted_dist = given_distance * 3280.84
    else:
        converted_dist = given_distance * 1093.61

    if time_unit == 'hr':
        converted_time = given_time
    elif time_unit == 'ms':
        converted_time = given_time * 3.6e+6
    elif time_unit == 's':
        converted_time = given_time * 3600
    elif time_unit == 'min':
        converted_time = given_time * 60
    else:
        converted_time = given_time * 0.0416667

    converted_speed = converted_dist / converted_time

    return round(converted_speed, 1)
    #print(f'converted_speed is {converted_speed}')