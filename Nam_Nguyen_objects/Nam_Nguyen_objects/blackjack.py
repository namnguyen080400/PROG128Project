#Assignment: blackjack.py
#Class: PROG 128
#Date: 06/05/2023
#Author: Nam Nguyen
#Description: Implement Blackjack object

#!/usr/bin/env python3

from Nam_Nguyen_objects import Card, Deck, Hand

class Blackjack:
    def __init__(self, startingBalance):
        self.currBalance = startingBalance
        self.bet = 0
        self.__deck = None
        self.__dealerhand = None
        self.__playerHand = None

    @property
    def playerHand(self):
        return self.__playerHand

    @property
    def dealerhand(self):
        return self.__dealerhand

    @property
    def deck(self):
        return self.__deck



    def displayCards(self,hand, title):
        ''' Print the title, print the cards and the points of the hand'''
        print(title)
        print()
        print(hand)
        print("Points: " + str(hand.points))

    def getBet(self):
        ''' Method to update self.bet by prompting the user for the bet amount,
        making sure bet is less than self.money.
        '''
        betAmount = int(input("Bet amount: "))
        while (betAmount <= 0 or betAmount > self.currBalance):
            if (betAmount <= 0):
                print("Invalid amount. Enter a positive number")
            else:
                print("You don't have enough money to make that bet.")
            betAmount = int(input("Bet amount: "))
        self.bet = betAmount

    def setupRound(self):
        ''' Setup the round by doing these steps:
        initialize self.deck to a new Deck object and shuffle it
        initialize self.dealerHand and self.playerHand to new Hand objects
        deal two cards to the playerHand, and one card to the dealerHand
        finally, print dealerHand and playerHand using displayCards method
        '''
        self.__deck = Deck()
        self.__deck.shuffle()
        self.__dealerhand = Hand()
        self.__dealerhand.addCard(self.__deck.dealCard())
        self.__playerHand = Hand()
        self.__playerHand.addCard(self.__deck.dealCard())
        self.__playerHand.addCard(self.__deck.dealCard())
        print()
        self.displayCards(self.__dealerhand, "DEALER'S SHOW CARD:")
        print()
        self.displayCards(self.__playerHand, "YOUR CARDS:")
    
        
    def takePlayerTurn(self):
        ''' Method to simulate player playing one turn by dealing a card
        to the player.'''
        print()
        print("Playing Player Hand...")

def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    # initialize starting money
    money = 100
    print("Starting Balance:", money)

    # instantiate object of Blackjack class 
    blackjack = Blackjack(money)
    
    print("Setting up a round...")
    # Call the getBet() and setupRound() methods of blackjack object
    # To be implemented in Phase 2
    blackjack.getBet()
    blackjack.setupRound()
    blackjack.takePlayerTurn()
    userMove = ""
    while (userMove != "s" and (not blackjack.playerHand.isBusted)):
        blackjack.takePlayerTurn()
        # To be implemented in Phase 2
        # Add code to play the player hand
        # Prompt the user to whether to Hit (h) or Stand (s)
        userMove = input("Hit or stand? (h for hit or s for stand): ").lower()
        print()
        # If player says stand,
        if (userMove == "s"):
            print()
            #      print player's points and exit
            print("YOUR POINTS: " + str(blackjack.playerHand.points))
        # else
        elif (userMove == "h"):
            blackjack.playerHand.addCard(blackjack.deck.dealCard())
            blackjack.displayCards(blackjack.playerHand, "YOUR CARDS:") 
            #    Check if the hand is busted, if so print player's points and exit
            if (blackjack.playerHand.isBusted):
                print()
                print("YOUR POINTS: " + str(blackjack.playerHand.points))
        else:
            print("Invalid input. The choice is (h for hit or s for stand)")
    print("Good bye!")


# if started as the main module, call the main function
if __name__ == "__main__":
    main()

