##IMPORTS
from random import choice

class Card:

    def __init__(self, suit, number):
        self._suit = suit
        self._number = number

    def __repr__(self):
        return self.number + " of " + self.suit
    
    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if number in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
            self._number = number
        else:
            print("That's not a number/picture card! "

##DECK CLASS
class Deck:

    ##__INIT__
    def __init__(self):
        self.supercomputer()

    ##POPULATE
    def populate(self):

        ##SUITS + NUMBERS
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

        ##DECK
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

    ##SHUFFLE
    def shuffle(self):

        ##CARDS SAVED BEFORE RESETTING 
        cards = self._cards
        self._cards = []

        ##WHEREITSHUFFLES
        while len(cards) > 0:

            card = choice(cards)
            self._cards.append(card)
            cards.remove(card)

            if cards == []:
                break
    ##CHECKING
    def CheckIfAllCardsAreThere(self):

        ##TAKING LENGTH OF DECK
        length = len(self._cards)

        ##IT HAS ALL CARDS
        if length == 52:
            print('It has all the 52 cards')

        ##IT IS MISSING CARDS
        elif length < 52:
            missing = 52 - length
            print('It is missing', str(missing), 'cards')
    ##DEAL
    def deal(self):

        ##PLAYERS
        player1 = []
        player2 = []
        player3 = []
        player4 = []

        ##HOW MUCH CARDS IN EACH DECK
        HMCIED = len(self._cards)//4

        ##PART WHERE IT DEALS
        for i in range(1, HMCIED):

            card = choice(self._cards)
            player1.append(card)
            self._cards.remove(card)

            card = choice(self._cards)
            player2.append(card)
            self._cards.remove(card)

            card = choice(self._cards)
            player3.append(card)
            self._cards.remove(card)

            card = choice(self._cards)
            player4.append(card)
            self._cards.remove(card)

    ##CONSOLE
    def console(self):
        print("You are now in the Deck of Cards console. Type Help to show the commands.")
        self.populate()
        while True:
            command = input("> ")

            if command == "Help":
                print("Commands: Help, to show the commands. Shuffle, shuffle the deck. Check cards, check the cards. Deal, deal the cards. Show cards, show the cards. Exit, exit the console and the shell.")

            elif command == "Shuffle":
                self.shuffle()
                print("Shuffled deck")

            elif command == "Check cards":
                self.CheckIfAllCardsAreThere()

            elif command == "Deal":
                self.deal()
                print("Dealed to 4 players")

            elif command == "Show cards":
                print(self._cards)

            elif command == "Exit":
                print("Exiting...")
                print("Press Okay")
                exit()
                      
            else:
                print("That is not a command! Type Help for a list of commands")
                      
my_deck = Deck()

