def non_repeats(n):
	n -=1
	res, v = n, n
	while n != 0:
		v = v*n
		res += v
		n -=1
	return res
