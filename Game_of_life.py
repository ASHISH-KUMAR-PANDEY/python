def game_of_life(board):
	resultstring=""
	xmax=len(board)
	ymax=len(board[0])
	for i in range(xmax):
		for j in range(ymax):
			neighbours=0
			#print(xmax,ymax)
			#print(i,j)
			for x in range(i-1,i+2):
				for y in range(j-1,j+2):
					#print(x,y)
					if x>=0 and x<xmax and y>=0 and y<ymax and not(x==i and y==j):
						#print("success")
						neighbours+=board[x][y]
			#print("i",i)
			#print("j",j)
			#print(neighbours)
			if board[i][j]==0:
				if neighbours==3:
					resultstring+="I"
				else:
					resultstring+="_"
			else:
				if neighbours<=1 or neighbours>=4:
					resultstring+="_"
				else:
					resultstring+="I"
		if i<xmax-1:
			resultstring+="\n"
	return resultstring
