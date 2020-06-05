def longest_substring(d):
	parity = ['x']+['o' if int(i)%2 else 'e' for i in d]+['x']
	repeats = [parity[i-1:i+2].count(parity[i]) for i in range(1,len(parity)-1)]
	indices = [i for i in range(len(repeats)) if (i in [0,len(repeats)-1] and repeats[i]==1) or (repeats[i]==2 and i in range(1, len(repeats)-1) and (repeats[i-1]==1 or repeats[i+1]==1))]
	subs = [d[indices[i]:indices[i+1]+1] for i in range(0,len(indices),2)]
	return max(subs,key=len)
