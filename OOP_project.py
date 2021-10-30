"""
    * OOP is a fundemental to becoming a good python programmer,
        so let's get some extra practice by bulding a game!

    * we will use OOP to create a cart game war!
"""

from random import Random, shuffle

# to useful variables for creating cards
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# mycards = [(s,r) for s in SUITE for r in RANKS]

# mycards = []
# for r in RANKS:
#     for s in SUITE:
#         mycards.append((s,r))

class Deck:
    """
    this is the Deck class. this object will create a deck of cards ti initiate play.
    tou can then use this deck list of cards to splite in half and give to the players.
    it will use SUITE and RUNKS to create the deck.
    it should also have a method for splitting/cutting the deck in hulf and shuffling the deck.
    """

    def __init(self):
        print("creating new ordered deck!")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print('shuffling the deck')
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand():
    """
    this is the Hand class, each player has a hand, and can add or remove cards from that hand.
    ther should be an add and remove card method here.
    """
    def __init__(self, cards) -> None:
        self.cards = cards

    def __str__(self) -> str:
        return 'contains {} cards'.format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player():
    """
    this is the Player class, wich takes in a name and an instance of a Hand class object.
    the player can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand) -> None:
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print('{} has plased: {} \n'.format(self.name, drawn_card))
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        """
        return true if player still has cards left
        """
        return len(self.hand.cards) != 0


######################
##### GAME PLAY ######
######################

print("welcome to war, let's begin...")

# create new deck and split in half:
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

# create both player
comp = Player('computer', Hand(half1))

name = input('wath is you name?')
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0


while user.still_has_cards and comp.still_has_cards():
    total_rounds += 1
    print('Time for a new round!')
    print('here are the carent standing')
    print(user.name + 'hase the count: ' + str(len(user.hand.cards)))
    print(comp.name + 'hase the count: ' + str(len(comp.hand.cards)))
    print('play a card! \n')

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print('war!')

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("game over, number of rounds: " + str(total_rounds))
print('a war happend ' + str(war_count) + ' times')
print('does the computer still have cards? ')
print(str(comp.still_has_cards()))
print('does the human still have cards? ')
print(str(user.still_has_cards()))