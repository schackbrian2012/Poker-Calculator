allSuits = ["Spades", "Hearts", "Diamonds", "Clubs"]
allNumbers = ["Ace", "Deuce", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]

def counts(numbers):
	return sorted([numbers.count(number) for number in set(numbers)])

def input(list, prompt):
	print ""
	for item in list:
		print list.index(item) + 1, item
	while not item.isdigit() or int(item) - 1 not in range(len(list)):
		item = raw_input(prompt)
	return list[int(item) - 1]
	
def straight(numbers):
	return set(numbers) in [set(allNumbers[i:i+5]) for i in range(len(allNumbers)-4)]

print ""
print "Poker Calculator"
print "Brian Schack"
suits = []
numbers = []
for card in range(5):
	suits.append(input(allSuits, "Suit? "))
	numbers.append(input(allNumbers[0:-1], "Number? "))
print ""
for card in range(5):
	print numbers[card] + " of " + suits[card]
print ""
if len(set(suits)) == 1 and straight(numbers):
	print "Straight Flush 0.0015%"
elif counts(numbers)[-1] == 4:
	print "Four of a Kind 0.024%"
elif counts(numbers) == [2, 3]:
	print "Full House 0.14%"
elif len(set(suits)) == 1:
	print "Flush 0.196%"
elif straight(numbers):
	print "Straight 0.39%"
elif counts(numbers)[-1] == 3:
	print "Three of a Kind 2.11%"
elif counts(numbers) == [1, 2, 2]:
	print "Two Pair 4.75%"
elif counts(numbers).count(2) == 1:
	print "One Pair 42.26%"
else:
	print "High Card 50.11%"
print ""