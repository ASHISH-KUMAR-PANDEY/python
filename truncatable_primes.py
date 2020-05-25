def truncatable(n):
	res = []

	if is_prime(n):
		n = str(n)
		
		if '0' not in n:
			if len(n) == 1:
				res += ['left','right']
			else:
				t_l = [int(n[-i:]) for i in range(1,len(n))]
				t_r = [int(n[:i]) for i in range(1,len(n))]
				if all(is_prime(n) for n in t_l):
					res.append('left')
				if all(is_prime(n) for n in t_r):
					res.append('right')
	
	return False if not res else 'both' if len(res) == 2 else res[0]

def is_prime(n):
	if n == 1:
		return False
	return not any(not n%i for i in range(2,n))
