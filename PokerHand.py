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



print(PokerHand())
