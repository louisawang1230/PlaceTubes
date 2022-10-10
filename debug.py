import numpy as np
def verify_location(location, tube, bowls):
	# location is the current location
	# tube is the chosen tube: -2, -1, 0, 1, 2
	direction = np.sign(tube)
	width = np.abs(tube)  # gives the size of the tube, either to left or right

	if direction > 0 and location + width > 7:
		return False
	if direction < 0 and location - width < 0:
		return False
	if width == 0:
		if bowls[location] != 10:
			return False
	for i in range(width+1):
		if bowls[location+i*direction] != 10:
			return False
	return True


print(verify_location(2, -1, [10, 10, 1, 1, 10, 10, 10, 10]))


# n = 6 hard coding

	tubes = [-2, -1, 0, 1, 2]
	bowls = [10, 10, 10, 10, 10, 10, 10, 10]

	bowl_location = np.random.choice(range(8))
	current_tube = np.random.choice(tubes)
for i in range(n):

def six():
	bowls = [0, 0, 0, 0, 0, 0, 0, 0]
	random_tube = np.random.choice(range(3))
	if random_tube == 2:
		random_location = np.random.choice(range(6))
		bowls[random_location] = 2
		bowls[random_location + 1] = 2
		bowls[random_location + 2] = 2
	elif random_tube == 1:
		random_location = np.random.choice(range(7))
		bowls[random_location] = 1
		bowls[random_location + 1] = 1
	else:
		empty_bowls = random.sample([0, 1, 2, 3, 4, 5, 6, 7], k=2)
		bowls[empty_bowls[0]] = 10
		bowls[empty_bowls[1]] = 10
	return bowls


