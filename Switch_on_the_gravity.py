def switch_gravity_on(lst):
	
	class Column:
	
		def __init__(self, col, pos):
			self.c = col
			self.p = pos
		
		def gravity(self):
			
			count = self.c.count('#')
			nonhash = len(self.c) - count
			
			new_col = []
			
			for n in range(nonhash):
				new_col.append('-')
			for n in range(count):
				new_col.append('#')
			
			self.c = new_col
			return True
	
	cols = []
	pos = []
	for n in range(len(lst[0])):
		col = []
		for row in lst:
			col.append(row[n])
		col = Column(col, n + 1)
		pos.append(n+1)
		cols.append(col)
	
	for col in cols:
		col.gravity()
	
	tr = []
	
	for item in lst:
		tr.append([])
	
	for n in range(len(lst[0])):
		pos = n+1
		for column in cols:
			if column.p == pos:
				col = column.c
				break
		for num in range(len(col)):
			tr[num].append(col[num])
	
	return tr
