from time import time
start = time()

def flush(hand):	#return = 100
	for x in range(1,5):
		if (hand[x])[1] != (hand[0])[1]:
			return 0
	return 100

def high_card(hand):	# return = value of the card
	highest = 0
	for x in hand:
		if x[0] == 'A':
			return 14
		elif x[0] == 'K':
			if highest < 13:
				highest = 13
		elif x[0] == 'Q':
			if highest < 12:
				highest = 12
		elif x[0] == 'J':
			if highest < 11:
				highest = 11
		elif x[0] == 'T':
			if highest < 10:
				highest = 10
		else:
			if highest < int(x[0]):
				highest = int(x[0])
	return highest

def staight(hand):	#return = 100+min_card
	card = 0
	s = []
	s_correct = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
	for x in hand:
		s.append(x[0])
	for y in range(0,10):
		if set(s_correct[y:y+5:]) == set(s):
			if '2' in set(s):
				card = 2
			elif '3' in set(s):
				card = 3
			elif '4' in set(s):
				card = 4
			elif '5' in set(s):
				card = 5
			elif '6' in set(s):
				card = 6
			elif '7' in set(s):
				card = 7
			elif '8' in set(s):
				card = 8
			elif '9' in set(s):
				card = 9
			elif 'T' in set(s):
				card = 10
			return 100+card
	return 0

def royal_flush(hand):	#return = 100
	if flush(hand) == 100:
		f = []
		f_correct = ['T','J','Q','K','A']
		for x in hand:
			f.append(x[0])
		if set(f)==set(f_correct):
			return 100
		else:
			return 0		
	else:
		return 0

def staight_flush(hand):	#return = 100+min_card
	k = staight(hand)
	if flush(hand)==100 and k >=100:
		return k
	else:
		return 0

def four_of_a_kind(hand):	#return = 100+card
	for x in range(0,2):
		count,card = 0,0
		for y in range(x+1,5):
			if (hand[x])[0] == (hand[y])[0]:
				count += 1
		if count == 3:
			if (hand[x])[0] == 'A':
				card = 14
			elif (hand[x])[0] == 'K':
				card = 13
			elif (hand[x])[0] == 'Q':
				card = 12
			elif (hand[x])[0] == 'J':
				card = 11
			elif (hand[x])[0] == 'T':
				card = 10
			else:
				card = int((hand[x])[0])
			return 100+card
	return 0

def three_of_a_kind(hand):	#return = 100+card
	for x in range(0,3):
		count,card = 0,0
		for y in range(x+1,5):
			if (hand[x])[0] == (hand[y])[0]:
				count += 1
		if count == 2:
			if (hand[x])[0] == 'A':
				card = 14
			elif (hand[x])[0] == 'K':
				card = 13
			elif (hand[x])[0] == 'Q':
				card = 12
			elif (hand[x])[0] == 'J':
				card = 11
			elif (hand[x])[0] == 'T':
				card = 10
			else:
				card = int((hand[x])[0])
			return 100+card
	return 0

def pairs(hand):		#if (no pairs -return 0 , if 1 pair -return 10000 , if 2 pairs -return 20000  )+card1*100 +card2*******
	for x in range(0,4):
		count1,count2,card1 = 0,0,0
		for y in range(x+1,5):
			if (hand[x])[0] == (hand[y])[0]:
				count1 = 1
				pair_string1 = (hand[x])[0]
				if pair_string1 == 'A':
					card1 = 14
				elif pair_string1 == 'K':
					card1 = 13
				elif pair_string1 == 'Q':
					card1 = 12
				elif pair_string1 == 'J':
					card1 = 11
				elif pair_string1 == 'T':
					card1 = 10
				else:
					card1 = int(pair_string1)
				break
		if count1 == 1:
			break
	if x==3 and count1 == 1:
		return 10000+card1*100
	elif x<3 and count1==1:
		for i in range(x+1,4):
			count2,card2 = 0,0
			for j in range(i+1,5):
				if (hand[i])[0] == (hand[j])[0]:
					count2 = 1
					pair_string2 = (hand[i])[0]
					if pair_string2 == 'A':
						card2 = 14
					elif pair_string2 == 'K':
						card2 = 13
					elif pair_string2 == 'Q':
						card2 = 12
					elif pair_string2 == 'J':
						card2 = 11
					elif pair_string2 == 'T':
						card2 = 10
					else:
						card2 = int(pair_string2)
					break
			if count2==1:
				break
		if count2==1:
			if card1>card2:
				return 20000+card1*100+card2
			elif card1<card2:
				return 20000+card2*100+card1
		return 10000+card1*100
	return 0

def full_house(hand):	# return 20000+ card
	k = pairs(hand)
	l = three_of_a_kind(hand)
	if l>=100 and k>=20000:
		if l-100 != (k-20000)%100:
			return 20000+(l-100)*100+(k-20000)%100
		elif l-100 != (k-20000)//100:
			return 20000+(l-100)*100+(k-20000)//100
	return 0

hand_list = open("54 Project Euler.txt","r")
player_1_wins = 0
for i in range(0,1000):
	hand = hand_list.readline(29).split(' ')
	hand_0 = hand_list.readline()		#to skip read "\n"
	hand_1 = hand[:5:]		#player 1 's hand
	hand_2 = hand[5::]		#player 2 's hand
	if royal_flush(hand_1) > royal_flush(hand_2):		
		player_1_wins += 1
	elif royal_flush(hand_1) == royal_flush(hand_2):
		if staight_flush(hand_1) > staight_flush(hand_2):		
			player_1_wins += 1
			print('vv')
		elif staight_flush(hand_1) == staight_flush(hand_2):
			if four_of_a_kind(hand_1) > four_of_a_kind(hand_2):		
				player_1_wins += 1
			elif four_of_a_kind(hand_1) == four_of_a_kind(hand_2):
				if full_house(hand_1) > full_house(hand_2):		
					player_1_wins += 1
				elif full_house(hand_1) == full_house(hand_2):
					if flush(hand_1) > flush(hand_2):		
						player_1_wins += 1
					elif flush(hand_1) == flush(hand_2):
						if staight(hand_1) > staight(hand_2):		
							player_1_wins += 1
						elif staight(hand_1) == staight(hand_2):
							if three_of_a_kind(hand_1) > three_of_a_kind(hand_2):		
								player_1_wins += 1
							elif three_of_a_kind(hand_1) == three_of_a_kind(hand_2):
								if pairs(hand_1) > pairs(hand_2):		
									player_1_wins += 1
								elif pairs(hand_1) == pairs(hand_2):
									if high_card(hand_1) > high_card(hand_2):		
										player_1_wins += 1
									elif high_card(hand_1) == high_card(hand_2):
										print("no answer", i+1)

print("player_1_wins ",player_1_wins)
hand_list.close()
print(time()-start , 'seconds')