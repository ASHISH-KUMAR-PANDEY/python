def encrypt(word):
	vowels = "aeou"
	rev = word[::-1]
	res = ""
	for l in rev:
		if l == "a" or l == "e" or l == "o" or l == "u":
