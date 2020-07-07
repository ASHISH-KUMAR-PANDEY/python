def josephus(n, i):
	c = [1]*n
	j = 0
	k = 0
	while sum(c)>0:
		if c[k]==1:
			j += 1
			if j == i:
				c[k] = 0
				j = 0
		k += 1
		if k == n:
			k = 0
	return k if k>0 else n
