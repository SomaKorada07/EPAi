from collections import namedtuple, Counter
import datetime
import re
import random
import string
from time import perf_counter
from functools import wraps
from faker import Faker


faker = Faker()


def timed(fn: "Function"):
    """
    Decorator to calculate run time of a function.
    """
    @wraps(fn)
    def calculate_time(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        time_elapsed = (end - start)
        print('Run time: {0:.4f}s'.format(time_elapsed))
        return result
    return calculate_time



def generate_fake_profiles_np(num_profiles: int):
	"""
	Function, takes a number as input and generates those many number
	of fake user profiles. Each of those profiles is stored as a named 
	tuple and a list of such namedtuples is returned.
	"""
	fake_profiles = []
	CreateProfiles = namedtuple('CreateProfiles', " ".join(list((faker.profile()).keys())))
	for _ in range(num_profiles):
		fake_profiles.append(CreateProfiles(**faker.profile()))
	return fake_profiles



@timed
def calculate_time_np() -> "namedtuple":
	"""
	Makes use of the generated profiles, stored in the form of list of named
	tuples and process the profiles to give some results. The results include
	the blood group with maximum occurance, mean location calculated from the
	location of all the profiles, person Oldest person with the profile and the
	average age.
	"""
	num_profiles = 10000
	fake_profiles = generate_fake_profiles_np(num_profiles)
	date_today = datetime.date.today()
	blood_group = dict()
	max_age = {'age': 0, 'proflie': None}
	cur_loc_coord_sum = [0, 0]
	sum_ages = 0
	for _ in fake_profiles:
		blood_group[_.blood_group] = blood_group[_.blood_group] + 1 if _.blood_group in blood_group else 1
		age = (date_today - _.birthdate).days
	if  age > max_age['age']:
		max_age['age'] = age
		max_age['profile'] = _
	cur_loc_coord_sum[0] += _.current_location[0]
	cur_loc_coord_sum[1] += _.current_location[1]
	sum_ages += int(age / 365)

	data = namedtuple('data', 'largest_blood_type mean_current_location oldest_person average_age')
	bg_l = max(blood_group, key = blood_group.get)
	mean_current_location = (cur_loc_coord_sum[0]/num_profiles, cur_loc_coord_sum[1]/num_profiles)
	return data((bg_l, blood_group[bg_l]), mean_current_location, (max_age['profile'], int(max_age['age']/365)), int(sum_ages/num_profiles))



def generate_fake_profiles_dict(num_profiles: int):
	"""
	Function, takes a number as input and generates those many number
	of fake user profiles. Each of those profiles is stored as a dictionary
	and a list of such dictionaries is returned.
	"""
	fake_profiles = []
	for _ in range(num_profiles):
		fake_profiles.append(faker.profile())
	return fake_profiles




@timed
def calculate_time_dict() -> "dictionary":
	"""
	Makes use of the generated profiles, stored in the form of list of dictionaries
	and process the profiles to give some results. The results include the blood
	group with maximum occurance, mean location calculated from the location of all
	the profiles, person Oldest person with the profile and the average age.
	"""
	num_profiles = 10000
	fake_profiles = generate_fake_profiles_dict(num_profiles)
	date_today = datetime.date.today()
	blood_group = dict()
	max_age = {'age': 0, 'proflie': None}
	cur_loc_coord_sum = [0, 0]
	sum_ages = 0
	for _ in fake_profiles:
		blood_group[_['blood_group']] = blood_group[_['blood_group']] + 1 if _['blood_group'] in blood_group else 1
		age = (date_today - _['birthdate']).days
	if  age > max_age['age']:
		max_age['age'] = age
		max_age['profile'] = _
	cur_loc_coord_sum[0] += _['current_location'][0]
	cur_loc_coord_sum[1] += _['current_location'][1]
	sum_ages += int(age / 365)
	bg_l = max(blood_group, key = blood_group.get)
	mean_current_location = (cur_loc_coord_sum[0] / num_profiles, cur_loc_coord_sum[1] / num_profiles)
	return {'largest_blood_type': (bg_l, blood_group[bg_l]), 'mean_current_location': mean_current_location, 'oldest_person': (max_age['profile'], int(max_age['age'] / 365)), 'average_age': int(sum_ages / num_profiles)}




def generate_companies(num_companies: int):
	"""
	Function takes number of companies as input and returns a list of named
	tuples, each of which is a Company data consisting of Name, Symbol Open,
	High, Close and Weight in given in the calculation of derivative index.
	"""
	companies = []
	weights = [round(random.random(), 5) for i in range(num_companies)]
	sum_weights = sum(weights)
	weights = [round(_/sum_weights, 5) for _ in weights]
	symbols = []
	Company = namedtuple('Company', 'Name Symbol Open High Close Weight')
	for _ in range(num_companies):
		co_name = faker.company()
		symbol = (''.join([i[0] for i in re.split('[,. ]+', co_name.replace("-", " "))])).lower()
		temp = ''
	while True:
		if symbol + temp not in symbols:
			symbols.append(symbol + temp)
		break
		temp = random.choice(string.ascii_lowercase)
	symbol += temp
	open = round(random.randint(1500, 5000) * random.uniform(1.0001, 1.0002), 2)
	high = round(open * random.uniform(1.0, 1.5), 2)
	high = high if high > open else open
	close = round(open * random.uniform(0.8, 1.75), 2)
	close = close if high > close else high
	companies.append(Company(co_name, symbol, open, high, close, weights[_]))
	return companies



def get_index(num_companies: int) -> "namedtuple":
	"""
	Generates and gives the Index open, high and close of a 
	small stock exchange simulation of listed stocks.
	input: num_companies, number of stocks in the exchange
	output: namedtuple('INDEX', 'Index_Open Index_High Index_Close')
	"""
	companies = generate_companies(num_companies)
	index_open = round(sum([_.Open * _.Weight for _ in companies]), 2)
	index_high = round(sum([_.High * _.Weight for _ in companies]), 2)
	index_close = round(sum([_.Close * _.Weight for _ in companies]), 2)
	INDEX = namedtuple('INDEX', 'Index_Open Index_High Index_Close')
	return INDEX(index_open, index_high, index_close)



get_index(100)