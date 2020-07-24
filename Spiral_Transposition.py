def spiral_transposition(lst):
	ans=[]
	for i in range(len(lst)):
		ans+=lst[i][i:len(lst[i])-i]
		print(ans)
		if len(ans)==len(lst[0])*len(lst):
			break
		for x in range(i+1,len(lst)-i):
			ans.append(lst[x][-(i+1)])
		print(ans)
		if len(ans)==len(lst[0])*len(lst):
			break
		ans+=(lst[-(i+1)][i:len(lst[i])-1-i])[::-1]
		print(ans)
		if len(ans)==len(lst[0])*len(lst):
			break
		for x in range(len(lst)-i-2,i,-1):
			ans.append(lst[x][i])
		print(ans)
		if len(ans)==len(lst[0])*len(lst):
			break
	return ans
