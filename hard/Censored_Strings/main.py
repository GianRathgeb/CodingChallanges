# Challange: https://edabit.com/challenge/ehyZvt6AJF4rKFfXT

# Input: uncensor("abcd", "") ➞ "abcd"

def uncensor(txt, vowels):
	replaced = 0
	output = ""
	for letter in txt:
		if letter == "*":
			output += str(vowels[replaced])
			replaced += 1
		else: output += str(letter)
	return output
