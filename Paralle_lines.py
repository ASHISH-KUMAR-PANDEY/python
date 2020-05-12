def lines_are_parallel(l1, l2):
	slope1 = (-l1[0]/l1[1])
	slope2 = (-l2[0]/l2[1])
	if slope1 == slope2:
		return True
	else:
		return False
