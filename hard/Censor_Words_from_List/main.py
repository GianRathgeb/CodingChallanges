# Challange: https://edabit.com/challenge/zJSF5EfPe69e9sJAc

# Input: censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

def censor_string(txt, lst, char):
	txt = txt.split(' ')
	for i, el in enumerate(txt):
		for j in lst:
			if el == j:
				replace = ""
				for x in range(0, len(el)):
					replace += char
				txt[i] = replace
	return ' '.join(txt)
