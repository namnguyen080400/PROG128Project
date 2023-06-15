#Assignment: objects.py
#Class: PROG 128
#Date: 06/05/2023
#Author: Nam Nguyen
#Description: Create three class objects: Card, Deck, and Hand

#!/usr/bin/env python3
import random
CARDS_CHARACTERS = {"Spades": "♠", "Hearts": "♥", "Diamonds": "♦", "Clubs": "♣"}
CARD_VALUE = {"2": 2, "3":3, "4": 4, "5":5, "6":6, "7":7, "8":8, "9":9,\
                                "10":10, "Jack":10, "Queen":10, "King":10, "Ace": 11}

##########################################################################
## Definitions for the classes: Card, Deck and Hand
##########################################################################

class Card:

    # constructor to initalized rank and suit
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit

    # set the public attribute for rank 
    # setter to check if card rank in invalid
    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, cardRank):
        if (self.__isValidRank(cardRank) == False):
            raise ValueError("Invalid card rank.")
        self.__rank = cardRank

    # set the public attribute for suit
    # setter to check if card suit in invalid
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, cardSuit):
        if (self.__isValidSuit(cardSuit) == False):
            raise ValueError("Invalid card suit.")
        self.__suit = cardSuit
    
    # private method __isValidSuit to check if suit valid return True. Otherwise return false
    def __isValidSuit(self, aSuit):
        if (aSuit in CARDS_CHARACTERS.keys()):
            return True
        return False

    # private method __isValidRank to check if suit valid return True. Otherwise return false
    def __isValidRank(self, aRank):
        if (aRank in CARD_VALUE.keys()):
            return True
        return False

    # readonly property value to return the card value rank
    @property
    def value(self):        
        return CARD_VALUE[self.rank]

    # method __str__ to print the card using print method
    def __str__(self):
        return self.rank + " of " + self.suit + " " + CARDS_CHARACTERS[self.suit] 

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __ne__(self, other):
        return self.rank != other.rank or self.suit != other.suit

    def __lt__(self, other):
        if (self.suit < other.suit):
            return True
        if (self.suit > other.suit):
            return False
        return self.rank < other.rank

    def __le__(self, other):
        if (self.suit < other.suit):
            return True
        if (self.suit > other.suit):
            return False
        return self.rank <= other.rank

    def __gt__(self, other):
        if (self.suit < other.suit):
            return True
        if (self.suit > other.suit):
            return False
        return self.rank > other.rank

    def __ge__(self, other):
        if (self.suit < other.suit):
            return True
        if (self.suit > other.suit):
            return False
        return self.rank >= other.rank


class Deck:
    # constructor to initalized deck to empty list. 
    # loop to refill card
    def __init__(self):
        self.__deck = []
        for suit in list(CARDS_CHARACTERS.keys()):
            for rank in list(CARD_VALUE.keys()):
                self.__deck.append(Card(rank, suit))

    # readonly property count to return how many card are in the deck

    def __len__(self):
        return len(self.__deck)

    # method shuffe to shuffle the card
    def shuffle(self):
        random.shuffle(self.__deck)

    # method dealCard to return the remove card
    def dealCard(self):
        if (len(self.__deck) > 0):
            return self.__deck.pop()
        return None

    def __iter__(self):
        for card in self.__deck:
            yield card

class Hand:

    # constructor to intialized empty cards list
    def __init__(self):
        self.__cards = []

    # readonly property count to set the length of the card

    def  __len__(self):
        return len(self.__cards)

    # readonly property points to increment the point
    @property
    def points(self):
        point = 0
        for card in self.__cards:
            if (card.value == 11):
                if (point + card.value > 21):
                    point += 1
                else:
                    point += 11
            else:
                point += card.value
        return point

    @property
    def isBusted(self):
        if (self.points > 21):
            return True
        return False

    @property
    def hasBlackjack(self):
        if (self.points == 21 and len(self.__cards) == 2):
            return True
        return False

    # method addCard to append the card
    def addCard(self, card):
        self.__cards.append(card)

    # method displayHand to loop to display the card
    def __str__(self):
        sortCards = sorted(self.__cards)
        result = ""
        for card in sortCards:
            result += card. __str__() + "\n"
        return result

    def shortDisplay(self):
        sortCards = sorted(self.__cards)
        result = ""
        for card in sortCards:
            result += card.__str__()
        return result

    def __iter__(self):
        for card in self.__cards:
            yield card
        
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

