# Plate calculator prototyping

weights = [
	[25, 20, 15, 10, 5, 2.5, 1.25],
	[55, 45, 35, 25, 10, 5, 2.5]
]

bar = 20


# Rounds down to the nearest plate
# 0: kg, 1: lbs
def calc(weight, unit=0):
	plates = []
	for w in weights[unit]:
		if (weight - (w * 2)) < 0:
			continue

		combined = w * 2
		left = weight % combined
		num = weight // combined

		plates += [w] * int(num)
		weight = left
		if weight == 0:
			break
	return plates


a = calc(100-bar)
print(a)
print(sum(a)*2 + bar)