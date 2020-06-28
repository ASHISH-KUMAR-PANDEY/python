rank = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

def is_pair(v):
	return v[0] == v[1] or v[1] == v[2] or v[2] == v[3] or v[3] == v[4]
	
def is_two_pair(v):
	s = set(v)
	return len(s) == 3
	
def three_right(v):
	return v[4] == v[3] == v[2]
def three_left(v):
	return v[0] == v[2] == v[3]
def three_mid(v):
	return v[1] == v[2] == v[3]
	
def is_three(v):
	return three_right(v) or three_left(v) or three_mid(v)
	
def is_full(v):
	return three_left(v) and v[3] == v[4] or three_right(v) and v[0] == v[1]

def four_left(v):
	return v[0] == v[1] and v[1] == v[2] and v[2] == v[3]
	
def four_right(v):
	return v[4] == v[3] and v[3] == v[2] and v[2] == v[1]



def is_four(v):
	return four_left(v) or four_right(v)
	
def is_flush(s):
	return s[0] == s[1] and s[1] == s[2] and s[2] == s[3] and s[3] == s[4]
	
def get_min(v):
	min = rank.index(v[0])
	for card in v[1:]:
		if rank.index(card) < min:
			min = rank.index(card)
	return min

def is_straight(v):
	min = get_min(v)
	return rank[min+1] in v and rank[min+2] in v and rank[min+3] in v and rank[min+4] in v

def is_straight_flush(v,s):
	return is_straight(v) and is_flush(s)

def is_royal_flush(v,s):
	return is_flush(s) and 'A' in v and 'K' in v and 'Q' in v and 'J' in v and '10' in v
def poker_hand_ranking(deck):
	values = [deck[0][:-1],deck[1][:-1],deck[2][:-1],deck[3][:-1],deck[4][:-1]]
	values.sort()
	suits = [deck[0][-1],deck[1][-1],deck[2][-1],deck[3][-1],deck[4][-1]]
	if is_royal_flush(values,suits):
		return "Royal Flush"
	if is_straight_flush(values,suits):
		return "Straight Flush"
	if is_four(values):
		return "Four of a Kind"
	if is_full(values):
		return "Full House"
	if is_flush(suits):
		return "Flush"
	if is_straight(values):
		return "Straight"
	if is_three(values):
		return "Three of a Kind"
	if is_two_pair(values):
		return "Two Pair"
	if is_pair(values):
		return "Pair"
	return "High Card"
