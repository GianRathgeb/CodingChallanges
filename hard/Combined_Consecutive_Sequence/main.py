# Challange: https://edabit.com/challenge/mHLAmj4vmRuXrT8Nb

# Input: consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

def consecutive_combo(lst1, lst2):
	for el in lst2:
		lst1.append(el)
	lst1.sort()
	for i, el in enumerate(lst1):
		if not i + 1 >= len(lst1):
			if el + 1 == lst1[i+1]: pass
			else: return False
	return True