# Challange: https://edabit.com/challenge/G9QRtAGXb9Cu368Pw

# Input: combinations(2, 3) ➞ 6

def combinations(*argv):
	result = 1
	for arg in argv:
		if not arg == 0:
			result = result * arg
	return result
