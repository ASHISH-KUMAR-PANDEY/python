def num_grid(lst):
	def increaseRisk(r, c):
		if r > len(lst) - 1 or r < 0 or c > len(lst[0]) - 1 or c < 0: return
		if lst[r][c] == '-': lst[r][c] = "0"
		if lst[r][c] != '#': lst[r][c] = str(int(lst[r][c]) + 1)
		
	def placeMine(r, c):
		dirs = [0, -1, 1]
		for x in range(-1, 2):
			for y in range(-1, 2):
				increaseRisk(r + y, c + x)
				
	for r in range(len(lst)):
		for c in range(len(lst[r])):
			if lst[r][c] == '-': lst[r][c] = "0"
			if lst[r][c] == '#':
				placeMine(r, c)
	return lst
