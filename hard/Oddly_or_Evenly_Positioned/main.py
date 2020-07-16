# Challange: https://edabit.com/challenge/KQe5w8AdSLbweW8ck

# Input: https://edabit.com/challenge/KQe5w8AdSLbweW8ck

def char_at_pos(r, s):
	output = []
	for i, el in enumerate(r):
		if s == "even":	
			if i % 2 != 0: 
				output.append(str(el))
		elif s == "odd": 
			if i % 2 == 0: 
				output.append(str(el))
	for i, el in enumerate(output):
		try:
			output[i] = int(el)
		except ValueError:
			pass
	if isinstance(r, list):
		return output
	else:
		output2 = ""
		for i in output:
			output2 += str(i)
		return output2