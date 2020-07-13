# Challange: https://edabit.com/challenge/PxxZprxCjDrzaTcLQ

# Input: vowel_links("a very large appliance") ➞ True

global vowels 
vowels = ["a", "e", "i", "o", "u"]
def check_vowel(str):
	for e in vowels:
		if str == e: 
			return True
	return False

def vowel_links(txt):
	for i, el in enumerate(txt):
		if i+2 < len(txt):
			if check_vowel(el) and txt[i+1] == " " and check_vowel(txt[i + 2]): 
				return True
	return False