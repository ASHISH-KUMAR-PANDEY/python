from math import sqrt

def triangle(perimeter,area):
	tris = []
	for a in range(1, perimeter//2+1):
		for b in range((perimeter-a)//2, a+1):
			#a>b>c
			c = perimeter-a-b
			cosine = (c*c - a*a - b*b)/(2*a*b)
			sine = sqrt(1 - cosine*cosine)
			if area == round(a*b*sine/2,5):
				if [b,c,a] not in tris and [c,b,a] not in tris:
					if b>c:
						tris.append([c,b,a])
					else:
						tris.append([b,c,a])
	return tris
