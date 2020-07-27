def dice_roll(n, outcome):
	if outcome<=0:
		return 0
	if n==1:
		if outcome<=6:
			return 1
		else:
			return 0
	if n>1:
		S=0
		for i in range(1,7):
			S=S+dice_roll(n-1,outcome-i)
		return S
