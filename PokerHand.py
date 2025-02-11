def PokerHand():
    list = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a"]
    hand = input ().lower ()
    cards = hand.split ()
    suits = []
    values = []
    for i in cards:
        r = i[::-1]
        suits.append (r[0])
        values.append (r[1::])
   
    pairs = []
    three = []
    four = []
    flush = suits.count (suits[0])
    for i in values:
        if values.count (i) == 2:
            pairs.append (i)
        elif values.count (i) == 3:
            three.append (i)
        elif values.count (i) == 4:
            four.append (i)

    sequence = []
    for i in values:
        if i == "01":
            j = i[::-1]
            sequence.append (list.index (j))
        else:
            sequence.append (list.index (i))
    sequence = sorted (sequence)
    royal = sequence[-1]
    diff = 0
    for i in range (len (sequence) - 1):
        royal += int (sequence[i])
        a = sequence[i + 1] - sequence[i]
        if a == 1 or a == 9:
            diff += 1

    if flush != 5 and len (pairs) == 2 and len (three) > 0:
        return "Full House"
    elif flush != 5 and len (pairs) == 2:
        return "One Pair"
    elif flush != 5 and len (pairs) == 4:
        return "Two Pairs"
    elif flush != 5 and len (three) > 0:
        return "Three of a Kind"
    elif flush != 5 and len (four) > 0:
        return "Four of a Kind"
    elif flush != 5 and diff == 4:
        return "Straight"
    elif flush == 5 and diff != 4:
        return "Flush"
    elif flush == 5 and diff == 4 and royal == 50:
        return "Royal Flush"
    elif flush == 5 and diff == 4:
        return "Straight Flush"
    else:
        return "High Card"

print(PokerHand())
