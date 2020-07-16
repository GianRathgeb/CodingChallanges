# Challange: https://edabit.com/challenge/D6XfxhRobdQvbKX4v

# Input: first_before_second("a rabbit jumps joyfully", "a", "j") ➞ True

def first_before_second(s, first, second):
	after = False
	for l in s:
		if after == True:
			if l == first: return False
		if l == second:
			after = True
	return True
