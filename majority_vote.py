def majority_vote(lst):
	if not lst:
		return None
	n = len(lst)
	max1 = max(lst, key=lst.count)
	newlst = [i for i in lst if i != max1]
	max2 = ''
	if len(newlst) > 0:
		max2 =  max(newlst, key=newlst.count)
	max1Count = lst.count(max1)
	max2Count = lst.count(max2)
	if max1Count > max2Count and max1Count > n/2:
		return max1
	return None
