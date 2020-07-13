# Challange: https://edabit.com/challenge/JzBLDzrcGCzDjkk5n

# Input: encrypt("banana") ➞ "0n0n0baca"

def encrypt(word):
	word = word[::-1]
	output = ""
	for l in word:
		if l == "a": output += "0"
		elif l == "e": output += "1"
		elif l == "i": output += "2"
		elif l == "o": output += "2"
		elif l == "u": output += "3"
		else: output += str(l)
	return output + "aca"