# Dictionary holding the number of each plate
weights = {
	25 : 0,
	20 : 2,
	15 : 1,
	10 : 1,
	5  : 1,
	2.5: 1
}


'''
Will attempt to get as close to the given weight as
possible with the available plates. Will round down
to the nearest possible weight.

<weight> is the target weight
<bar> is the barbell weight (assumes standard 20kg)

OUTPUT:
Returns list of plates required for one side of the
bar. Load each side equally.
'''
def calc(weight, bar=20, weights=weights):
	weight -= bar
	plates = []
	for w in weights:
		# Ignores plate if it exceeds weight cap
		if (weight - (w * 2)) < 0:
			continue

		# Ensures plate pair is available
		if weights[w] == 0:
			continue

		combined = w * 2
		num = weight // combined
		if weights[w] >= num:
			plates += [w] * int(num)
			weight -= combined * int(num)
		else:
			plates += [w] * weights[w]
			weight -= combined * weights[w]

	return plates

bar = 20

a = calc(100)
print(a)
print((sum(a) * 2) + bar)