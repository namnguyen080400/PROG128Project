#!/usr/bin/env python3
from Nam_Nguyen_objects import Card, Hand, Deck

        
def main():
    print("Cards - Tester")
    print()

    #test sorting of the cards
    testcardsList = [Card("Ace", "Spades"), Card("Queen", "Hearts"), Card("10", "Clubs"),
             Card("3", "Diamonds"), Card("Jack", "Hearts"), Card("7", "Spades")]
    testcardsList.sort()
    print("TEST CARDS LIST AFTER SORTING.")
    for c in testcardsList:
        print(c)
    print()

    # test deck
    print("DECK")
    deck = Deck()
    print("Deck created.")
    deck.shuffle()    
    print("Deck shuffled.")
    print("Deck count:", len(deck))
    print()

    # test hand
    hand = Hand()
    for i in range(10):
        hand.addCard(deck.dealCard())

    print("SORTED HAND")
    print(hand)

    print()
    print("Hand points:", hand.points)
    print("Hand count:", len(hand))
    print("Deck count:", len(deck))

if __name__ == "__main__":
    main()

