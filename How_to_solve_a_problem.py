# Problem under observation
# Given your bithday and the current date, calculate your age in days.
# Compensate for leap days. Assume that birthday and current dates(and no time travel)
# Simply put, if you were born 1 Jan 2012 and todays date is 2 Jan 2012 your are 1 day old

# Attempt 01 (COMPLETE MESS :( )
# def check_leap_year(year):
# 	if year % 4 == 0:
# 		# if year % 100 == 0:
# 		# 	if year % 400 == 0:
# 		return True
# 	return False

# def age(y1, m1, d1, y2, m2, d2):
# 	check_leap = check_leap_year(y1)
# 	total_years = y2 - y1
# 	total_months = m2 - m1
# 	total_days = (d2 - d1) 
# 	for i in range(y1, y2 + 1):
# 		print(i)
# 		check_leap = check_leap_year(i)
# 		if check_leap: 
# 			total_days += 1
# 			print(total_days)
# 	age_in_days = total_days + (total_months * 30) + (total_years * 12 * 30)
# 	return f"You are {age_in_days} old!"
# print(age(1992, 11, 12, 2019, 11, 26))


# The first thing we should do to solve a problem like this?
# 1.Make sure we understand the problem
# 2.Search Google for the answer if it is not the practice problem
# 3.Work out an algo that solves it
# 4.Start Writing Code

# 1. Understanding the problem
# Ques. Understand what are the inputs?
# Ans. Your bithday and the current date(Two Dates)
# * no time travel: current date comes after birthday
# * Gregorian Calendar (15 Oct 1582)

# Ques: How are inputs represented?
# Ans: def daysBetweenDates(year1, month1, day1, year2, month2, day2)

# Ques: Whar are the outputs?
# Ans.Return a number giving the number of days between the first date and second date

# 3.Work out an algo that solves it
# Work out some examples
# daysBetweenDates(2012, 12, 7, 2012, 12, 7): 0
# daysBetweenDates(2012, 12, 7, 2012, 12, 8): 1
# daysBetweenDates(2012, 12, 8, 2012, 12, 7): Undefined
# daysBetweenDates(2012, 6, 29, 2013, 6, 29): 365
# daysBetweenDates(2012, 6, 29, 2013, 6, 31): Undefined

# Algo pseudocode
# Brain dead approach
# days = 0
# while date1 is before date2:
# 	date1 = advance in next date
# 	days += 1
# return days

# What should we do first?
# * nextDay(year, month, day): to get next day for a simple case
# * dateIsBefore(year1, month1, day1, year2, month2, day2): check if date 1 is before date2
# * isLeapYear(year): to determine if year is leap year
# The year can be evenly divided by 4;If the year can be evenly divided by 100, it is NOT a leap year, unless;
# The year is also evenly divisible by 400. Then it is a leap year.e.g. 1800, 1900 not leap years

# Attempt 02
def isLeapYear(year):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
		return False
	elif year % 4 == 0:
		return True
	else:
		return False

def daysInMonth(year, month):
	if month in [1,3,5,7,8,10,12]:
		return 31 
	else:
		if month == 2:
			if isLeapYear(year):
				return 29
			else:
				return 28
		else:
			return 30

# nextDay(year, month, day): Assume all months have 30 days
def nextDay(year, month, day):
	if day < daysInMonth(year, month):
		return year, month, day+1
	else: 
		if month < 12:
			return year, month + 1, 1
		else:
			return year + 1, 1, 1 
	return year
print(nextDay(2019, 12, 30))	# (2020, 1, 1)
print(nextDay(2019, 11, 30))	# (2019, 12, 1)
print(nextDay(2019, 1, 30))		# (2019, 2, 1)

def dateIsBefore(y1, m1, d1, y2, m2, d2):
	if y1 < y2:
		return True
	if y1 == y2:
		if m1 < m2:
			return True
		if m1 == m2:
			return d1 < d2
	return False


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
	days = 0
	while dateIsBefore(y1, m1, d1, y2, m2, d2):
		y1, m1, d1 = nextDay(y1, m1, d1)
		days += 1
	return days
print(daysBetweenDates(2020, 11, 12, 2019, 11, 26))	# 0
print(daysBetweenDates(1992, 11, 12, 2019, 11, 26))	# 9875