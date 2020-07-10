def isWordChain(words):
	if len(words)<2:
		return True
	previous_word = words[0]
	for i in range(1,len(words)):
		if is_levelshtein_1(previous_word, words[i]):
			previous_word = words[i]
		else:
			return False
	return True

def is_levelshtein_1(a,b):
	len_diff = len(a) - len(b)
	if len_diff > 1 or len_diff < -1:
		return False
	
	#case 1
	if len_diff == 0:
		change_count = 0
		for i in range(len(a)):
			if a[i] == b[i]:
				continue
			else:
				change_count = change_count+1
		return change_count == 1
		
	#case 2
	if len_diff == 1:
		longer = a
		shorter = b
	else:
		longer = b
		shorter = a
	remove_char_found = 0
	for i in range(len(shorter)):
		if shorter[i-remove_char_found] == longer[i]:
			continue
		else:
			remove_char_found = remove_char_found+1
	return remove_char_found <2
