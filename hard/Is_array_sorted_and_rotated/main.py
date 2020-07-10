# Challange: https://edabit.com/challenge/KEsQGp7LsP3KwmqJ7

# Input: check([3, 4, 5, 1, 2]) ➞ "YES"
# Input: check([1, 2, 3]) ➞ "NO"

def check(arr):
	sorted_arr = sorted(arr)
	for i in range(0, len(sorted_arr)):
		correct_counter = 0
		for j in range(0, len(arr)):
			print("ARR: {} SORTARR: {}".format(arr, sorted_arr))
			if arr[j] == sorted_arr[j]:
				correct_counter += 1
				if correct_counter == len(arr):
					if i != 0: return "YES"
					else: return "NO"
				continue
		sorted_arr.append(sorted_arr[0])
		sorted_arr.remove(sorted_arr[0])
	return "NO"