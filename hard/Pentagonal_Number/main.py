# Challange: https://edabit.com/challenge/st8mDxreMcuWxuz8c

# Input: pentagonal(8) ➞ 141

def pentagonal(num):
	if num == 1: dots =  1
	elif num == 2: dots = 6
	else:
		dots = 6
		for n in range(2, num):
			dots += 5 * n
	return dots	
