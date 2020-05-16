def pentagonal(num,res=1,n=1):
	if n == 1:
		res = 1
	else:
		res += 5*(n-1)

	if n == num:
		return res
	else:
		n += 1
		return pentagonal(num,res,n)
