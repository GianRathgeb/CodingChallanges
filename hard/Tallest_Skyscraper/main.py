# Challange: https://edabit.com/challenge/76ibd8jZxvhAwDskb

""" tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]) ➞ 3 """

def combinations(*argv):
	result = 1
	for arg in argv:
		if not arg == 0:
			result = result * arg
	return result
