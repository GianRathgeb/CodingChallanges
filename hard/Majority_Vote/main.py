# Challange: https://edabit.com/challenge/pQavNkBbdmvSMmx5x

# Input: majority_vote(["A", "A", "B"]) ➞ "A"
# Input: majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None

def majority_vote(lst):
	if len(lst) != 0:
		count = {}
		for i in lst:
			if i in count: count[i] += 1
			else: count[i] = 1
		major_votes = max(count.values())
		major = [k for k, v in count.items() if v == major_votes]
		if len(major) > 1: return None
		else: return major[0]
	else: return None