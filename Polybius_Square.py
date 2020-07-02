dic = {
"11": "a", "12": "b", "13":"c", "14": "d", "15": "e",
"21": "f", "22": "g", "23":"h", "24": "i", "25": "k",
"31": "l", "32": "m", "33":"n", "34": "o", "35": "p",
"41": "q", "42": "r", "43":"s", "44": "t", "45": "u",
"51": "v", "52": "w", "53":"x", "54": "y", "55": "z"}

def polybius(text):
	result = []
	if text[0] in "0123456789":
		ind = 0
		while ind < len(text) - 1:
			if text[ind] == " ":
				result.append(" ")
				ind = ind+1
			elif text[ind] not in "12345":
				ind = ind+1
			elif text[ind:ind+2] in dic:
				result.append(dic[text[ind:ind+2]])
				ind = ind+2
			else:
				raise
	else:
		reverse = {}
		for key,value in dic.items():
			reverse[value] = key
		reverse["j"] = "24"
		for i in text:
			if i == " ":
				result.append(" ")
			if i.lower() in reverse:
				result.append(reverse[i.lower()])
	return "".join(result)
