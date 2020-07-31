import numpy as np
def diamond(carat):
	even = False
	cut = 'perfect cut'
	if not (carat % 2):
			carat +=1
			even = True

	diamond = np.zeros([carat,carat])
	edge_len = carat // 2 + 1
	edges = np.ones([edge_len,edge_len])
	for row in range(1,edge_len-1):
			for col in range(1,edge_len-1):
					edges[row, col] = 0

	n = edge_len-1
	for ii in range(0, edge_len):
			for jj in range(0, edge_len):
					diamond[ii+jj,-ii+jj+n] = edges[ii,jj]

	if even:
		cut = 'good cut'
		diamond = np.delete(diamond,edge_len-1,1)
		diamond = np.delete(diamond,carat-1,0)
		diamond = np.delete(diamond,0,0)
		
	return [diamond.tolist(), cut]
