def emphasise(string):
	s = ''
	for i in range(len(string)):
		if i == 0:
			s += string[i].upper()
		elif string[i - 1] != " ":
			s += string[i].lower() 
		else:
			s += string[i].upper()
	return s
