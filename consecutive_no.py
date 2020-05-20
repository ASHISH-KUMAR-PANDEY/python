def areAscendingNumbers(txt, numdigits):
	first = int(txt[0:numdigits])
	for i in range(1, len(txt)//numdigits):
		if int(txt[i*numdigits:(i+1)*numdigits]) != (first + i):
			return False
	return True
	
def ascending(txt):
	if len(txt) <= 1:
		return False
	for numdigits in range(1, len(txt)//2 + 1):
		if len(txt) % numdigits == 0:
			if areAscendingNumbers(txt, numdigits):
				return True
	return False
