# Challange: https://edabit.com/challenge/zzibM5MaxDNvQCrEk

# Input: will_fit(["M", "L", "L", "M"], [56, 62, 84, 90]) ➞ True

def will_fit(holds, cargo):
	spaces = []
	space_left = []
	cargo_fits = []
	next_cargo = False
	for h in holds:
		if h == "S": spaces.append(50)
		elif h == "M": spaces.append(100)
		elif h == "L": spaces.append(200)
	spaces.sort(reverse=True)
	cargo.sort(reverse=True)
	for x in cargo:
		for y in spaces:
			if x <= y:
				space_left.append(y - x)
				spaces.remove(y)
				next_cargo = True
				break
		if next_cargo:
			next_cargo = False
			continue
		for z in space_left:
			if x <= z:
				space_left.append(z - x)
				try:
					spaces.remove(z)
				except ValueError:
					# Do nothing, cause nothing in Spaces
					pass
				next_cargo = True
				break
		if next_cargo:
			next_cargo = False
			continue
		return False
	return True