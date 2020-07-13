# Challange: https://edabit.com/challenge/Xkc2iAjwCap2z9N5D

# Input: has_friday_13(3, 2020) ➞ True

import datetime
def has_friday_13(month, year):
	start_day = datetime.datetime(year=2014, month=month, day=1)
	end_day = datetime.datetime(year=2014, month=month+1, day=1)
	days = (end_day - start_day).days
	for i in range(0, days):
		date = datetime.date(year, month, i + 1)
		if date.strftime("%A") == "Friday" and i + 1 == 13:
				return True
	return False