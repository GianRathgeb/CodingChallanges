# Challange: https://edabit.com/challenge/QoavwQhmrDpXJhBW9

# Input: flip_list([1, 2, 3, 4]) ➞ [[1], [2], [3], [4]]

def flip_list(lst):
	output = []
	for i in lst:
		if type(i) is list:
			output.append(i[0])
		elif type(i) is int:
			output.append([i])
	return output
